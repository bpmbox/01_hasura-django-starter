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
      <p>{{message}}</p>
      <input type="text" v-model="inputWord" @focus="focus"/>
      <button @click="changeButtonStatus">検索</button>
    </div>
    <div class="result-display-area">
      <div v-for="(item, $index) in list" :key="$index">
        {{item.title}} ( {{item['dc:creator']}} )
      </div>
    </div>
    <infinite-loading spinner="spiral" @infinite="infiniteHandler" v-if="buttonStatus">
      <span slot="no-more">----- 検索結果は以上です-----</span>
　　　 <span slot="no-results">----- 検索結果はありません-----</span>
    </infinite-loading>
  </section>
</template>

<script>
import axios from 'axios';
import InfiniteLoading from 'vue-infinite-loading';

let url = 'https://ci.nii.ac.jp/books/opensearch/search?title=';

export default {
  components: {
    InfiniteLoading
  },
  data() {
    return {
      inputWord: '',
      buttonStatus: false,
      page: 1,
      list: [],
      message: ''
    }
  },
  methods: {
    changeButtonStatus() {
      if(!this.inputWord) {
        this.message = 'Please input some word.'
        return;
      }
      this.buttonStatus = true
    },
    infiniteHandler($state) {
      axios.get((url + this.inputWord), {
        params: {
          p: this.page,
          format: 'json'
        }
      }).then(({data}) => {
        const items = data['@graph'][0]['items'];
        setTimeout(() => {
          if(items) {
            this.page += 1;
            this.list.push(...items)
            $state.loaded();
          } else {
            $state.complete();
          }
        }, 1000)
      }).catch((error) => {
        this.message = 'error'
      })
    },
    focus() {
      this.inputWord = '';
      this.buttonStatus = false,
      this.page = 1;
      this.list = [];
      this.message = '';
    }
  }
}
</script>
