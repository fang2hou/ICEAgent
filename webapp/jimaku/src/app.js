// API site
const config = {
  timeout: 500,
  baseURL: 'http://127.0.0.1:1688'
}
httpRequest = axios.create(config);

var JimakuMain = new Vue({
  el: "#rc-main-container",
  data: {
    subtitle: '',
	startButton: {
      isShown: true,
      text: 'Start',
    },
  },
  methods: {
    startMonitor: function () {
      window.setInterval(() => {
        setTimeout(() => {
          httpRequest.get("/icetts/get/subtitle").then(response => {
            if (response.data == "") { return; }
            this.subtitle = response.data;
          })
        }, 0)
      }, config.timeout)
    },
	
	generateSession: function () {
		this.startMonitor();
        this.startButton.isShown = false;
	},
  }
});