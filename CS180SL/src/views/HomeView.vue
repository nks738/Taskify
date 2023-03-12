<script lang="ts">
import { defineComponent, ref, reactive, toRaw, watch } from "vue";
import {
  HomeOutlined,
  SettingOutlined,
  UserOutlined,
} from "@ant-design/icons-vue";
import dayjs from "dayjs";
import { message } from "ant-design-vue";
import type { Dayjs } from "dayjs";
import type { FormInstance } from "ant-design-vue";

import ScheduleDetail from "@/components/ScheduleDetail.vue";

interface FormState {
  id?: number;
  date?: Dayjs[];
  title?: string;
}

interface State {
  list: FormState[];
}

export default defineComponent({
  components: {
    HomeOutlined,
    SettingOutlined,
    UserOutlined,
    ScheduleDetail,
  },
  setup() {
    const current = ref<string[]>(["home"]);
    const calendarMode = ref<string>("month");
    const value = ref<Dayjs>();
    const visible = ref<boolean>(false);
    const formRef = ref<FormInstance>();
    const uniqueKey = ref<number>(Date.now());
    const formState = reactive<FormState>({
      id: undefined,
      title: "",
      date: undefined,
    });
    const state = reactive<State>({
      list: JSON.parse(localStorage.getItem("list") || "[]"),
    });

    watch(state, async (newValue) => {
      localStorage.setItem("list", JSON.stringify(newValue.list));
    });

    const getListData = (value: Dayjs, data: State) => {
      const list = data.list.filter((item) => {
        return dayjs(value).isBetween(
          item.date?.[0],
          item.date?.[1],
          "day",
          "[]"
        );
      });
      return (
        list?.map((item, index) => ({
          ...item,
          key: `${item.id}-${index}-${value.format("YYYY-MM-DD")}`,
          type: "success",
        })) || []
      );
    };

    const getMonthData = (value: Dayjs) => {
      console.log(value);
      return null;
    };

    const onSelect = (value: Dayjs) => {
      if (calendarMode.value === "month") {
        formState.date = [value, value];
        formState.title = "";
        formState.id = undefined;
        visible.value = true;
      }
    };

    const handleOk = () => {
      formRef.value
        ?.validateFields()
        .then((values) => {
          visible.value = false;
          formRef.value?.resetFields();
          if (values.id) {
            // edit
            state.list = state.list.map((item) => {
              if (item.id === values.id) {
                return {
                  ...toRaw(values),
                  id: values.id,
                };
              }
              return item;
            });
          } else {
            uniqueKey.value = Date.now();
            // add
            state.list = [
              ...state.list,
              {
                ...toRaw(values),
                id: uniqueKey.value,
              },
            ];
          }
          message.success("Added successfully");
        })
        .catch((info) => {
          console.log("Validate Failed:", info);
        });
    };

    const onPanelChange = (value: Dayjs, mode: string) => {
      calendarMode.value = mode;
    };

    const deleteSchedule = (schedule: FormState) => {
      state.list = [...state.list.filter((item) => item.id !== schedule.id)];
      message.success("Delete succeeded");
    };

    const editSchedule = (schedule: FormState) => {
      visible.value = true;
      formState.date = schedule.date;
      formState.title = schedule.title;
      formState.id = schedule.id;
    };

    return {
      current,
      visible,
      handleOk,
      value,
      state,
      getListData,
      getMonthData,
      onSelect,
      onPanelChange,
      calendarMode,
      formRef,
      formState,
      deleteSchedule,
      editSchedule,
    };
  },
});
</script>

<template>
  <a-layout class="home-container">
    <a-layout-sider>
      <div class="logo">Schedule management</div>
      <a-menu v-model:selectedKeys="current" mode="inline">
        <a-menu-item key="home">
          <HomeOutlined />
          <span>Home</span>
        </a-menu-item>
        <a-menu-item key="setting">
          <SettingOutlined />
          <span>Setting</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header>
        <a-dropdown>
          <a-avatar style="background-color: #87d068">
            <template #icon>
              <UserOutlined />
            </template>
          </a-avatar>
          <template #overlay>
            <a-menu>
              <a-menu-item>
                <a href="/login">Logout</a>
              </a-menu-item>
            </a-menu>
          </template>
        </a-dropdown>
      </a-layout-header>
      <a-layout-content>
        <a-modal
          v-model:visible="visible"
          :mode="calendarMode"
          title="Create Schedule"
          @ok="handleOk"
        >
          <a-form
            ref="formRef"
            :model="formState"
            name="form_in_modal"
            layout="vertical"
            autocomplete="off"
          >
            <a-form-item
              label="Date"
              name="date"
              :rules="[{ required: true, message: 'Please pick your date!' }]"
            >
              <a-range-picker
                v-model:value="formState['date']"
                value-format="YYYY-MM-DD"
              />
            </a-form-item>
            <a-form-item
              name="title"
              label="Title"
              :rules="[{ required: true, message: 'Please input your title!' }]"
            >
              <a-input v-model:value="formState.title" />
            </a-form-item>
            <a-form-item hidden name="id">
              <a-input />
            </a-form-item>
          </a-form>
        </a-modal>
        <a-calendar
          v-model:value="value"
          @select="onSelect"
          @panelChange="onPanelChange"
        >
          <template #dateCellRender="{ current }">
            <ul class="events">
              <li
                v-for="item in getListData(current, state)"
                v-bind:key="item.key"
              >
                <schedule-detail
                  @remove="deleteSchedule"
                  @edit="editSchedule"
                  :item="item"
                />
              </li>
            </ul>
          </template>
          <template #monthCellRender="{ current }">
            <div v-if="getMonthData(current)" class="notes-month">
              <section>{{ getMonthData(current) }}</section>
            </div>
          </template>
        </a-calendar>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<style lang="less" scoped>
.home-container {
  width: 100vw;
  height: 100vh;
  overflow: auto;

  aside {
    background-image: linear-gradient(to top, #5ee7df 0%, #b490ca 100%);

    .logo {
      background: linear-gradient(
        to right,
        pink,
        orange,
        yellow,
        green,
        cyan,
        blue,
        purple
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: hue 3s linear infinite;
      font-size: 20px;
      font-weight: 700;
      padding: 16px;
    }

    .ant-menu {
      border: none;
      background: transparent;
    }
  }

  .ant-layout-header {
    text-align: end;
    padding-right: 16px;
    background-color: #fff;
  }

  .ant-avatar-icon {
    cursor: pointer;
  }

  .ant-layout-content {
    margin: 24px 16px;
    padding: 24px;
    background-color: #fff;
    overflow: auto;
  }

  .ant-picker-calendar-full {
    width: 1000px;
    margin: auto;
  }

  .events {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .events .ant-badge-status {
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
    text-overflow: ellipsis;
    font-size: 12px;
  }
  .notes-month {
    text-align: center;
    font-size: 28px;
  }
  .notes-month section {
    font-size: 28px;
  }
}

@keyframes hue {
  0% {
    filter: hue-rotate(0deg);
  }
  100% {
    filter: hue-rotate(360deg);
  }
}
</style>
