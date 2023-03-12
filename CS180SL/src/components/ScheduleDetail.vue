<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import {
  EditOutlined,
  DeleteOutlined,
  CloseOutlined,
} from "@ant-design/icons-vue";
import dayjs from "dayjs";

export default defineComponent({
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  emits: ["remove", "edit"],
  components: {
    EditOutlined,
    DeleteOutlined,
    CloseOutlined,
  },
  setup(props, context) {
    const visible = ref<boolean>(false);
    const schedule = ref(props.item);

    watch(
      () => props.item,
      (newValue) => {
        schedule.value = newValue;
      }
    );

    const hide = () => {
      visible.value = false;
    };

    const onRemove = () => {
      hide();
      context.emit("remove", schedule.value);
    };

    const onEdit = () => {
      hide();
      context.emit("edit", schedule.value);
    };

    return {
      visible,
      hide,
      schedule,
      startDate: [
        dayjs(schedule.value.date?.[0]).format("YYYY-MM-DD"),
        `(${dayjs(schedule.value.date?.[0]).format("dddd")})`,
      ].join(""),
      endDate: [
        dayjs(schedule.value.date?.[1]).format("YYYY-MM-DD"),
        `(${dayjs(schedule.value.date?.[1]).format("dddd")})`,
      ].join(""),
      onRemove,
      onEdit,
    };
  },
});
</script>

<template>
  <a-popover placement="leftTop" trigger="click" v-model:visible="visible">
    <template #title>
      <div class="schedule-detail">
        <span> Schedule Detail </span>
        <a-space>
          <edit-outlined @click="onEdit" />
          <a-popconfirm
            title="Are you sure delete this schedule?"
            ok-text="Yes"
            cancel-text="No"
            @confirm="onRemove"
          >
            <delete-outlined />
          </a-popconfirm>
          <close-outlined @click="hide" />
        </a-space>
      </div>
    </template>
    <template #content>
      <unordered-list-outlined /> Title: {{ schedule.title }}
      <br />
      <field-time-outlined /> Date: {{ startDate }}
      <span v-if="startDate !== endDate">
        ~
        {{ endDate }}
      </span>
    </template>
    <a-badge :status="schedule.type" :text="schedule.title" @click.stop />
  </a-popover>
</template>

<style scoped>
.schedule-detail {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
