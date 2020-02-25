//将此代码粘贴到工具中
!function(t) {
    function n(e) {
        if (r[e]) return r[e].exports;
        var i = r[e] = {
            exports: {},
            id: e,
            loaded: !1
        };
        return t[e].call(i.exports, i, i.exports, n),
        i.loaded = !0,
        i.exports
    }
    var r = {};
    return n.m = t,
    n.c = r,
    n.p = "",
    n(0)
} ([function(t, n, r) {
    r(1)(window)
},
function(t, n) {
    t.exports = function(t) {
        var n = "RealXMLHttpRequest";
        t.hookAjax = function(t) {
            function r(n) {
                return function() {
                    var r = this.hasOwnProperty(n + "_") ? this[n + "_"] : this.xhr[n],
                    e = (t[n] || {}).getter;
                    return e && e(r, this) || r
                }
            }
            function e(n) {
                return function(r) {
                    var e = this.xhr,
                    i = this,
                    o = t[n];
                    if ("function" == typeof o) e[n] = function() {
                        t[n](i) || r.apply(e, arguments)
                    };
                    else {
                        var u = (o || {}).setter;
                        r = u && u(r, i) || r;
                        try {
                            e[n] = r
                        } catch(t) {
                            this[n + "_"] = r
                        }
                    }
                }
            }
            function i(n) {
                return function() {
                    var r = [].slice.call(arguments);
                    if (!t[n] || !t[n].call(this, r, this.xhr)) return this.xhr[n].apply(this.xhr, r)
                }
            }
            return window[n] = window[n] || XMLHttpRequest,
            XMLHttpRequest = function() {
                var t = new window[n];
                for (var o in t) {
                    var u = "";
                    try {
                        u = typeof t[o]
                    } catch(t) {}
                    "function" === u ? this[o] = i(o) : Object.defineProperty(this, o, {
                        get: r(o),
                        set: e(o),
                        enumerable: !0
                    })
                }
                this.xhr = t
            },
            window[n]
        },
        t.unHookAjax = function() {
            window[n] && (XMLHttpRequest = window[n]),
            window[n] = void 0
        },
        t.
    default = t
    }
}]);
hookAjax(
        // hook functions and callbacks of XMLHttpRequest object
        {
            onreadystatechange: function (xhr) {
                //console.log("onreadystatechange called: %O", xhr)
                
            },
            onload: function (xhr) {
                //console.log("onload called: %O", xhr)
                xhr.responseText = "hook" + xhr.responseText;
                
            },
            open: function (arg, xhr) {
                console.log("open called: method:%s,url:%s,async:%s", arg[0], arg[1], arg[2], xhr)
                arg[1] += "?hook_tag=1";
                //统一添加请求头
            },
            send: function (arg, xhr) {
                //console.log("send called: %O", arg[0])
                xhr.setRequestHeader("_custom_header_", "ajaxhook")
            },
            setRequestHeader: function (arg, xhr) {
                //console.log("setRequestHeader called!", arg)
            },
            // hook attributes of XMLHttpRequest object
            timeout: {
                setter: function (v, xhr) {
                    //timeout shouldn't exceed 10s
                    return Math.max(v, 1000);
                }
            }
        }
    );