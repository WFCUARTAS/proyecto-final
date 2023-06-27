let app = new Vue({
    el: '#app',
    data() {
      return {
        titulo:'sdase',
        exclusivas:null,
        mejores: null
      }
    },
    methods: {
      deleteTask(){
        this.tareas = this.tareas.filter(t => !t.isDone)
      }
    },
    async mounted () {

        const url = "http://127.0.0.1:8000/";
        var result = await fetch(url+"exclusivas");
        var data = await result.json();
        this.exclusivas = data;

        var result = await fetch(url+"mejores");
        var data = await result.json();
        this.mejores = data;

    }
                
  })