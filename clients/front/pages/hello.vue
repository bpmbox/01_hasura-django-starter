<template>
  <div>
    <div>
      <v-btn @click="hello">HELLO</v-btn>
    </div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ""
    }
  },
  methods: {
    hello() {
      let data = this.$data;
      this.$axios.get("/api/hello")
        .then(res => {
          data.message = res.data["Hello"];
        })
        .catch((e) => {
          console.error(e);
        })
    }
  }
}
</script>
