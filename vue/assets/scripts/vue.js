let app = new Vue({
    el: '#app',
    data() {
      return {
        titulo:'sdase',
        exclusivas:[],
        mejores: [],
        blogs:[]
      }
    },
    methods: {
      deleteTask(){
        this.tareas = this.tareas.filter(t => !t.isDone)
      }
    },
    async mounted () {

        const url = "http://127.0.0.1:8000/";

        var result_e = await fetch(url+"exclusivas");
        var data_e = await result_e.json();
        this.exclusivas = data_e;

        var result_m = await fetch(url+"mejores");
        var data_m = await result_m.json();
        this.mejores = data_m;

        var result_b = await fetch(url+"blogs");
        var data_b = await result_b.json();
        this.blogs = data_b;
    }
                
  })