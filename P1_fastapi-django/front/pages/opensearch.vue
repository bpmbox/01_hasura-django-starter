<template>
  <section class="container">
    <style type="text/css">
      input.example1,
      select {
        width: 250px;
      }
      textarea {
        width: 250px;
        height: 7em;
      }

      input,
      select,
      textarea {
        background-color: #bde9ba;
      }
      option.example2 {
        background-color: #ffffff;
      }
    </style>
    <div class="input-area">
      <p>{{ message }}{{qquery}}{{page}}</p>
      <input type="text" v-model="inputWord" @focus="focus" />
      <button @click="changeButtonStatus">title検索</button>
      <input type="text" v-model="limit" @focus="focus" />
      <button @click="changeButtonStatus">limit</button>
      <input type="text" v-model="offset" @focus="focus" />
      <button @click="changeButtonStatus">offset</button>

    </div>
      <div class="input-area">
      <p>{{ message }}{{qquery}}{{page}}</p>
      <input type="text" v-model="inputWodddrd" @focus="focus" width="300" />
      <button @click="changeButtonStatus">Bearer</button>
    </div>
    <div class="result-display-area">
      <div v-for="(item, $index) in list" :key="$index">
        {{ item }}
        {{item.page}}
        {{ item.title }} ( {{ item["dc:creator"] }} )
      </div>
    </div>
    <infinite-loading
      @infinite="infiniteHandler"
      v-if="buttonStatus"
    ></infinite-loading>
  </section>
</template>

<script>
import axios from "axios";
import InfiniteLoading from "vue-infinite-loading";

let url = "/library/_search";
const query = {
  query: {
    match_all: {},
  },
};
export default {
  token: "aaaaaa",
  components: {
    InfiniteLoading,
  },
  data() {
    return {
      inputWord: "",
      buttonStatus: false,
      page: 1,
      list: [],
      message: "",
      token: "aaaaaa",
      limit: 1,
      offset: 1,
      qquery: JSON.stringify(query)
    }
  },
  methods: {
    changeButtonStatus() {
      if (!this.inputWord) {
        this.message = "Please input some word.";
        return;
      }
      this.buttonStatus = true;
    },
    infiniteHandler($state) {
      console.log(this.token);
      // axios.get((url + this.inputWord), {
      axios
        .get(url, {
          //} + this.inputWord), {

          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          //  headers: {
          //    Authorization: `Bearer ${token}`,
          //},
          auth: {
            username: "admin",
            password: "admin",
          },
          params: {
            source: JSON.stringify({
  "query": {
    "bool": {
      "must": [
          {
          "wildcard": {
            "title": "*"+this.inputWord+"*"
          }
        }
      ]
    }
  }
}),
            source_content_type: "application/json",
          },
        })
        .then(({ data }) => {
          console.log(data);
          console.log(data["hits"]["hits"]);
          const items = data["hits"]["hits"]; //['@graph'][0]['items'];
          if (items) {
            this.page += 1;
            this.list.push(...items);
            $state.loaded();
          } else {
            $state.complete();
          }
        })
        .catch((error) => {
          console.log(error);
          this.message = "error";
        });
    },
    focus() {
      this.inputWord = "";
      (this.buttonStatus = false), (this.page = 1);
      this.list = [];
      this.message = "";
    },
  },
};
</script>
