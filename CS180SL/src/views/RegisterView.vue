<script lang="ts">
import { defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";

interface FormState {
  username: string;
  password: string;
  remember: boolean;
}
export default defineComponent({
  setup() {
    const router = useRouter();
    const formState = reactive<FormState>({
      username: "",
      password: "",
      remember: true,
    });
    const onFinish = (values: any) => {
      console.log("Success:", values);
      router.push("/");
    };

    const onFinishFailed = (errorInfo: any) => {
      console.log("Failed:", errorInfo);
    };
    return {
      formState,
      onFinish,
      onFinishFailed,
    };
  },
});
</script>

<template>
  <main>
    <div class="left-banner"></div>
    <div class="register-form">
      <a-form
        :model="formState"
        name="basic"
        :colon="false"
        hideRequiredMark
        layout="vertical"
        autocomplete="off"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
      >
        <h2>Register</h2>
        <h4>Manage all your schedules efficiently</h4>
        <a-form-item
          label="Username"
          name="username"
          :rules="[{ required: true, message: 'Please input your username!' }]"
        >
          <a-input v-model:value="formState.username" />
        </a-form-item>

        <a-form-item
          label="Password"
          name="password"
          :rules="[{ required: true, message: 'Please input your password!' }]"
        >
          <a-input-password v-model:value="formState.password" />
        </a-form-item>

        <a-form-item name="remember">
          <a-checkbox v-model:checked="formState.remember"
            >I agree to all the <a>Term</a>, <a>Privacy Policy</a></a-checkbox
          >
        </a-form-item>

        <a-form-item>
          <a-button type="primary" html-type="submit">Create Account</a-button>
        </a-form-item>

        <p>
          Already have an account?
          <router-link to="/login">Log in</router-link>
        </p>
      </a-form>
    </div>
  </main>
</template>

<style lang="less" scoped>
main {
  display: flex;
  width: 100vw;
  height: 100vh;
}

.left-banner {
  width: 40%;
  background-image: linear-gradient(to top, #a6c1ee 0%, #fbc2eb 100%);
}

.register-form {
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: start;

  form {
    width: 400px;
    h2 {
      width: 100%;
      margin-bottom: 50px;
    }

    h4 {
      margin-bottom: 30px;
    }

    button {
      width: 100%;
    }
  }
}
</style>
