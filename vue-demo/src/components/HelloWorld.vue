<template>
  <div class="hello">
    <h3>学习Vue：模板语法</h3>
    <p>{{ message }}</p>

    <p>Message is: {{ message1 }}</p>
    <input v-model="message1" placeholder="edit me" />
    <p>Using text interpolation: {{ rawHtml }}</p>
    <p>Using v-html directive: <span v-html="rawHtml"></span></p>
    <div v-bind:id="dynamicId"></div>
    <div :id="dynamicId2"></div>
    <p>{{ num+10 }}</p>
    <p>{{ flag?"niubi":"shabi" }}</p>
    <div v-bind="objectOfAttrs"></div>
    <p v-if="seen">Now you see me</p>
    <p v-else>Now you cant see me</p>
    <p v-show="seen">Now you cant see me</p>
    <ul>
      <li v-for="item in items" :key="index">
        {{ item.message }}
      </li>
    </ul>
    <button @click="count++">Add 1</button>
    <p>Count is: {{ count }}</p>
    <button @click="greet">Greet</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data(){
    return{
      message: "学习vue",
      message1: "学习vue gogogo",
      rawHtml: "<a href='https://www.google.com'>谷歌</a>",
      dynamicId: 10001,
      dynamicId2: 10002,
      num: 10,
      flag:true,
      objectOfAttrs: {
        id: 'container',
        class: 'wrapper'
      },
      seen: true,
      items: [{ message: 'Foo' }, { message: 'Bar' }],
      count: 0
    }
  },
  methods: {
    greet(event) {
      // 方法中的 `this` 指向当前活跃的组件实例
      alert(`Hello ${this.message}!`)
      // `event` 是 DOM 原生事件
      if (event) {
        console.log(event)
      }
    }
  }
}
</script>

