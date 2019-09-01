exports.config = {
  seleniumAddress: 'http://localhost:4444/wd/hub',
  specs: ['get_expences_table.js'],
  capabilities: {
  		'browserName': 'firefox'
	},
   onPrepare: function(){
   browser.manage().timeouts().implicitlyWait(5000);
	}
};