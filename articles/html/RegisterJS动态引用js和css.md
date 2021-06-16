# RegisterJS动态引用js和css

RegisterJS用于原生前端页面，用于动态加载js和css文件，比如用于以下场景：

+ 动态加载js语言包文件，如：zh_CN.js, en_US.js
+ 页面中的某些js和css需要延时加载

## 1 RegisterJS

```javascript
var register = (function() {

    var resources = []; // {src:"", type: "js/css", loaded: false/true}

    var registJs = function(src, onload) {
        var s = document.createElement('script');
        s.type = 'text/javascript';
        s.src = src;
        s.onload = onload;
        document.body.appendChild(s);
    };

    var registCss = function(href, onload) {
        var s = document.createElement('link');
        s.rel = 'stylesheet';
        s.href = href;
        s.onload = onload;
        document.body.appendChild(s);
    };

    var regist = function(index, callback) {
        var len = resources.length;
        // 全部加载完成
        if (index >= len) {
            console.log("[registerjs] All Loaded");
            if (callback)
                callback();
            return;
        }
        if (!resources[index].loaded) {
            if (resources[index].type == "js")
                registJs(resources[index].src, function() {
                    resources[index].loaded = true;
                    console.log("[registerjs] " + resources[index].src + " loaded!");
                    regist(index + 1, callback);
                });
            if (resources[index].type == "css")
                registCss(resources[index].src, function() {
                    resources[index].loaded = true;
                    console.log("[registerjs] " + resources[index].src + " loaded!");
                    regist(index + 1, callback);
                });
        } else
            regist(index + 1, callback);
    };

    var load = function(config, callback) {
        if (!config)
            return;
        if (config.js)
            for (var i in config.js) {
                var isExist = resources.filter(function(value) {
                    return value.src == config.js[i]
                }).length > 0;
                if (!isExist)
                    resources.push({
                        src: config.js[i],
                        type: "js",
                        loaded: false
                    });
            }
        if (config.css)
            for (var i in config.css) {
                var isExist = resources.filter(function(value) {
                    return value.src == config.css[i]
                }).length > 0;
                if (!isExist)
                    resources.push({
                        src: config.css[i],
                        type: "css",
                        loaded: false
                    });
            }
        regist(0, callback);
    };

    return {
        load: load
    }
})();
```

## 2 使用示例

```javascript
window.onload = function() {
    register.load({
        js: [
            "vendors/jquery-2.1.3.min.js",
            "utility/Utility.js",
            "vendors/vue.min.js",
            "vendors/element-ui/element-ui.min.js",
            "components/TableComponent.js"
        ],
        css: [
            "vendors/element-ui/element-ui.min.css"
        ]
    }, main);
}

function main() {
    var app = new Vue({
        el: '#div_Main',
        data: {
            files: files
        }
    });
}
```

