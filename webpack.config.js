var webpack = require("webpack");
var path = require("path");
var HtmlWebpackPlugin = require("html-webpack-plugin");

//module.exports
module.exports = {
	// devtool:"eval-source-map",
	entry:__dirname+"/app/main.js", //加载入口文件
	// entry:{
	// 	page1: __dirname+"/app/main.js",
     //    page2: ["./entry1", "./entry2"]
	// },
	output:{  //输出文件	
		path:__dirname+"/build",
		filename:"bundle.js"
	},

	module:{
		loaders:[
			//配置json格式的转换
			{
				test:/\.json$/,
				loader:"json"
			},
			// {
			// 	test:/\.js$/,
			// 	exclude:"node_modules",
			// 	loader:"babel",
			// 	query:{
			// 		presets:["es2015","react"]
			// 	}
			// },
			{
				test:/\.css$/,
				loader:"style!css"
				//！的意思是同一个文件用两种方案去处理
			}
		]
	},

	//插件
	plugins:[
		new webpack.ProvidePlugin({
			  $:"jquery",
			  jQuery:"jquery",
			  "window.jQuery":"jquery"
    	}),
		new HtmlWebpackPlugin({
			filename: 'index.html',
			template:__dirname+"/app/templates/index.html"
		})
	]
}