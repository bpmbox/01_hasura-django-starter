export default function ({ $axios, redirect }) {
  $axios.onRequest(config => {
    console.log("axios config", config)
  })
}