_signature: n
var n = u(m.getUri(e), e);
function u(e, t) {
    var n, r, a = "".concat(location.protocol, "//").concat(location.host);
    (function(e) {
        return !l.some((function(t) {
            return e.indexOf(t) > -1
        }
        ))
    }
    )(e) && (a += "/toutiao");
    var o = {
        url: a + e
    };
    return t.data && (o.body = t.data),
    (null === (r = null === (n = window.byted_acrawler) || void 0 === n ? void 0 : n.sign) || void 0 === r ? void 0 : r.call(n, o)) || ""
    window.byted_acrawler.sign.call(n, o)
    window.byted_acrawler.sign(o)
    o = {url: 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc'}
}