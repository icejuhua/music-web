const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
const webpack = require('webpack')
module.exports = {
	chainWebpack: (config) => {
		config.plugin('provide').use(webpack.ProvidePlugin, [{
			$: 'jquery',
			jquery: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery'
		}])
	},
	css: {
		sourceMap: true
	}
}