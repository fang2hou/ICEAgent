// API site
const config = {
  timeout: 500,
  baseURL: 'http://127.0.0.1:1688'
}
httpRequest = axios.create(config);

var JimakuMain = new Vue({
  el: "#rc-main-container",
  data: {
    subtitle: {
        text: '',
        fontSize: 25,
    },
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
            this.subtitle.text = response.data;
          })
          httpRequest.get("/icetts/get/subtitle/pitch").then(response => {
            if (response.data == "") { return; }
            // base font size is 20.
            // the scale size is 30.
            var LOW = -6;
            var HIGH = 6;
            this.subtitle.fontSize = 20 + Math.round(30 * (parseFloat(response.data)-LOW)/(HIGH - LOW));
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