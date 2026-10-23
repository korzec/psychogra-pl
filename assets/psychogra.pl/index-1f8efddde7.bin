jQuery(document).ready(function($){$('.mpp-gutenberg-tab').on('click',function(e){$('.mpp-author-tabs li').removeClass('active');$(this).addClass('active');var $tabs=$('.mpp-tab').removeClass('mpp-tab-active');var new_tab=$(this).data('tab');$('.'+new_tab).addClass('mpp-tab-active');});});
;/*!
 * jQuery UI Mouse 1.13.3
 * https://jqueryui.com
 *
 * Copyright OpenJS Foundation and other contributors
 * Released under the MIT license.
 * https://jquery.org/license
 */
!function(e){"use strict";"function"==typeof define&&define.amd?define(["jquery","../ie","../version","../widget"],e):e(jQuery)}(function(o){"use strict";var n=!1;return o(document).on("mouseup",function(){n=!1}),o.widget("ui.mouse",{version:"1.13.3",options:{cancel:"input, textarea, button, select, option",distance:1,delay:0},_mouseInit:function(){var t=this;this.element.on("mousedown."+this.widgetName,function(e){return t._mouseDown(e)}).on("click."+this.widgetName,function(e){if(!0===o.data(e.target,t.widgetName+".preventClickEvent"))return o.removeData(e.target,t.widgetName+".preventClickEvent"),e.stopImmediatePropagation(),!1}),this.started=!1},_mouseDestroy:function(){this.element.off("."+this.widgetName),this._mouseMoveDelegate&&this.document.off("mousemove."+this.widgetName,this._mouseMoveDelegate).off("mouseup."+this.widgetName,this._mouseUpDelegate)},_mouseDown:function(e){var t,i,s;if(!n)return this._mouseMoved=!1,this._mouseStarted&&this._mouseUp(e),i=1===(this._mouseDownEvent=e).which,s=!("string"!=typeof(t=this).options.cancel||!e.target.nodeName)&&o(e.target).closest(this.options.cancel).length,i&&!s&&this._mouseCapture(e)&&(this.mouseDelayMet=!this.options.delay,this.mouseDelayMet||(this._mouseDelayTimer=setTimeout(function(){t.mouseDelayMet=!0},this.options.delay)),this._mouseDistanceMet(e)&&this._mouseDelayMet(e)&&(this._mouseStarted=!1!==this._mouseStart(e),!this._mouseStarted)?e.preventDefault():(!0===o.data(e.target,this.widgetName+".preventClickEvent")&&o.removeData(e.target,this.widgetName+".preventClickEvent"),this._mouseMoveDelegate=function(e){return t._mouseMove(e)},this._mouseUpDelegate=function(e){return t._mouseUp(e)},this.document.on("mousemove."+this.widgetName,this._mouseMoveDelegate).on("mouseup."+this.widgetName,this._mouseUpDelegate),e.preventDefault(),n=!0)),!0},_mouseMove:function(e){if(this._mouseMoved){if(o.ui.ie&&(!document.documentMode||document.documentMode<9)&&!e.button)return this._mouseUp(e);if(!e.which)if(e.originalEvent.altKey||e.originalEvent.ctrlKey||e.originalEvent.metaKey||e.originalEvent.shiftKey)this.ignoreMissingWhich=!0;else if(!this.ignoreMissingWhich)return this._mouseUp(e)}return(e.which||e.button)&&(this._mouseMoved=!0),this._mouseStarted?(this._mouseDrag(e),e.preventDefault()):(this._mouseDistanceMet(e)&&this._mouseDelayMet(e)&&(this._mouseStarted=!1!==this._mouseStart(this._mouseDownEvent,e),this._mouseStarted?this._mouseDrag(e):this._mouseUp(e)),!this._mouseStarted)},_mouseUp:function(e){this.document.off("mousemove."+this.widgetName,this._mouseMoveDelegate).off("mouseup."+this.widgetName,this._mouseUpDelegate),this._mouseStarted&&(this._mouseStarted=!1,e.target===this._mouseDownEvent.target&&o.data(e.target,this.widgetName+".preventClickEvent",!0),this._mouseStop(e)),this._mouseDelayTimer&&(clearTimeout(this._mouseDelayTimer),delete this._mouseDelayTimer),this.ignoreMissingWhich=!1,n=!1,e.preventDefault()},_mouseDistanceMet:function(e){return Math.max(Math.abs(this._mouseDownEvent.pageX-e.pageX),Math.abs(this._mouseDownEvent.pageY-e.pageY))>=this.options.distance},_mouseDelayMet:function(){return this.mouseDelayMet},_mouseStart:function(){},_mouseDrag:function(){},_mouseStop:function(){},_mouseCapture:function(){return!0}})});
;/*!
 * jQuery UI Slider 1.13.3
 * https://jqueryui.com
 *
 * Copyright OpenJS Foundation and other contributors
 * Released under the MIT license.
 * https://jquery.org/license
 */
!function(e){"use strict";"function"==typeof define&&define.amd?define(["jquery","./mouse","../keycode","../version","../widget"],e):e(jQuery)}(function(o){"use strict";return o.widget("ui.slider",o.ui.mouse,{version:"1.13.3",widgetEventPrefix:"slide",options:{animate:!1,classes:{"ui-slider":"ui-corner-all","ui-slider-handle":"ui-corner-all","ui-slider-range":"ui-corner-all ui-widget-header"},distance:0,max:100,min:0,orientation:"horizontal",range:!1,step:1,value:0,values:null,change:null,slide:null,start:null,stop:null},numPages:5,_create:function(){this._keySliding=!1,this._mouseSliding=!1,this._animateOff=!0,this._handleIndex=null,this._detectOrientation(),this._mouseInit(),this._calculateNewMax(),this._addClass("ui-slider ui-slider-"+this.orientation,"ui-widget ui-widget-content"),this._refresh(),this._animateOff=!1},_refresh:function(){this._createRange(),this._createHandles(),this._setupEvents(),this._refreshValue()},_createHandles:function(){var e,t=this.options,i=this.element.find(".ui-slider-handle"),s=[],a=t.values&&t.values.length||1;for(i.length>a&&(i.slice(a).remove(),i=i.slice(0,a)),e=i.length;e<a;e++)s.push("<span tabindex='0'></span>");this.handles=i.add(o(s.join("")).appendTo(this.element)),this._addClass(this.handles,"ui-slider-handle","ui-state-default"),this.handle=this.handles.eq(0),this.handles.each(function(e){o(this).data("ui-slider-handle-index",e).attr("tabIndex",0)})},_createRange:function(){var e=this.options;e.range?(!0===e.range&&(e.values?e.values.length&&2!==e.values.length?e.values=[e.values[0],e.values[0]]:Array.isArray(e.values)&&(e.values=e.values.slice(0)):e.values=[this._valueMin(),this._valueMin()]),this.range&&this.range.length?(this._removeClass(this.range,"ui-slider-range-min ui-slider-range-max"),this.range.css({left:"",bottom:""})):(this.range=o("<div>").appendTo(this.element),this._addClass(this.range,"ui-slider-range")),"min"!==e.range&&"max"!==e.range||this._addClass(this.range,"ui-slider-range-"+e.range)):(this.range&&this.range.remove(),this.range=null)},_setupEvents:function(){this._off(this.handles),this._on(this.handles,this._handleEvents),this._hoverable(this.handles),this._focusable(this.handles)},_destroy:function(){this.handles.remove(),this.range&&this.range.remove(),this._mouseDestroy()},_mouseCapture:function(e){var i,s,a,n,t,h,l=this,u=this.options;return!u.disabled&&(this.elementSize={width:this.element.outerWidth(),height:this.element.outerHeight()},this.elementOffset=this.element.offset(),t={x:e.pageX,y:e.pageY},i=this._normValueFromMouse(t),s=this._valueMax()-this._valueMin()+1,this.handles.each(function(e){var t=Math.abs(i-l.values(e));(t<s||s===t&&(e===l._lastChangedValue||l.values(e)===u.min))&&(s=t,a=o(this),n=e)}),!1!==this._start(e,n))&&(this._mouseSliding=!0,this._handleIndex=n,this._addClass(a,null,"ui-state-active"),a.trigger("focus"),t=a.offset(),h=!o(e.target).parents().addBack().is(".ui-slider-handle"),this._clickOffset=h?{left:0,top:0}:{left:e.pageX-t.left-a.width()/2,top:e.pageY-t.top-a.height()/2-(parseInt(a.css("borderTopWidth"),10)||0)-(parseInt(a.css("borderBottomWidth"),10)||0)+(parseInt(a.css("marginTop"),10)||0)},this.handles.hasClass("ui-state-hover")||this._slide(e,n,i),this._animateOff=!0)},_mouseStart:function(){return!0},_mouseDrag:function(e){var t={x:e.pageX,y:e.pageY},t=this._normValueFromMouse(t);return this._slide(e,this._handleIndex,t),!1},_mouseStop:function(e){return this._removeClass(this.handles,null,"ui-state-active"),this._mouseSliding=!1,this._stop(e,this._handleIndex),this._change(e,this._handleIndex),this._handleIndex=null,this._clickOffset=null,this._animateOff=!1},_detectOrientation:function(){this.orientation="vertical"===this.options.orientation?"vertical":"horizontal"},_normValueFromMouse:function(e){var t,e="horizontal"===this.orientation?(t=this.elementSize.width,e.x-this.elementOffset.left-(this._clickOffset?this._clickOffset.left:0)):(t=this.elementSize.height,e.y-this.elementOffset.top-(this._clickOffset?this._clickOffset.top:0)),e=e/t;return(e=1<e?1:e)<0&&(e=0),"vertical"===this.orientation&&(e=1-e),t=this._valueMax()-this._valueMin(),e=this._valueMin()+e*t,this._trimAlignValue(e)},_uiHash:function(e,t,i){var s={handle:this.handles[e],handleIndex:e,value:void 0!==t?t:this.value()};return this._hasMultipleValues()&&(s.value=void 0!==t?t:this.values(e),s.values=i||this.values()),s},_hasMultipleValues:function(){return this.options.values&&this.options.values.length},_start:function(e,t){return this._trigger("start",e,this._uiHash(t))},_slide:function(e,t,i){var s,a=this.value(),n=this.values();this._hasMultipleValues()&&(s=this.values(t?0:1),a=this.values(t),2===this.options.values.length&&!0===this.options.range&&(i=0===t?Math.min(s,i):Math.max(s,i)),n[t]=i),i!==a&&!1!==this._trigger("slide",e,this._uiHash(t,i,n))&&(this._hasMultipleValues()?this.values(t,i):this.value(i))},_stop:function(e,t){this._trigger("stop",e,this._uiHash(t))},_change:function(e,t){this._keySliding||this._mouseSliding||(this._lastChangedValue=t,this._trigger("change",e,this._uiHash(t)))},value:function(e){if(!arguments.length)return this._value();this.options.value=this._trimAlignValue(e),this._refreshValue(),this._change(null,0)},values:function(e,t){var i,s,a;if(1<arguments.length)this.options.values[e]=this._trimAlignValue(t),this._refreshValue(),this._change(null,e);else{if(!arguments.length)return this._values();if(!Array.isArray(e))return this._hasMultipleValues()?this._values(e):this.value();for(i=this.options.values,s=e,a=0;a<i.length;a+=1)i[a]=this._trimAlignValue(s[a]),this._change(null,a);this._refreshValue()}},_setOption:function(e,t){var i,s=0;switch("range"===e&&!0===this.options.range&&("min"===t?(this.options.value=this._values(0),this.options.values=null):"max"===t&&(this.options.value=this._values(this.options.values.length-1),this.options.values=null)),Array.isArray(this.options.values)&&(s=this.options.values.length),this._super(e,t),e){case"orientation":this._detectOrientation(),this._removeClass("ui-slider-horizontal ui-slider-vertical")._addClass("ui-slider-"+this.orientation),this._refreshValue(),this.options.range&&this._refreshRange(t),this.handles.css("horizontal"===t?"bottom":"left","");break;case"value":this._animateOff=!0,this._refreshValue(),this._change(null,0),this._animateOff=!1;break;case"values":for(this._animateOff=!0,this._refreshValue(),i=s-1;0<=i;i--)this._change(null,i);this._animateOff=!1;break;case"step":case"min":case"max":this._animateOff=!0,this._calculateNewMax(),this._refreshValue(),this._animateOff=!1;break;case"range":this._animateOff=!0,this._refresh(),this._animateOff=!1}},_setOptionDisabled:function(e){this._super(e),this._toggleClass(null,"ui-state-disabled",!!e)},_value:function(){var e=this.options.value;return this._trimAlignValue(e)},_values:function(e){var t,i;if(arguments.length)return e=this.options.values[e],this._trimAlignValue(e);if(this._hasMultipleValues()){for(t=this.options.values.slice(),i=0;i<t.length;i+=1)t[i]=this._trimAlignValue(t[i]);return t}return[]},_trimAlignValue:function(e){var t,i;return e<=this._valueMin()?this._valueMin():e>=this._valueMax()?this._valueMax():(t=0<this.options.step?this.options.step:1,i=e-(e=(e-this._valueMin())%t),2*Math.abs(e)>=t&&(i+=0<e?t:-t),parseFloat(i.toFixed(5)))},_calculateNewMax:function(){var e=this.options.max,t=this._valueMin(),i=this.options.step;(e=Math.round((e-t)/i)*i+t)>this.options.max&&(e-=i),this.max=parseFloat(e.toFixed(this._precision()))},_precision:function(){var e=this._precisionOf(this.options.step);return e=null!==this.options.min?Math.max(e,this._precisionOf(this.options.min)):e},_precisionOf:function(e){var e=e.toString(),t=e.indexOf(".");return-1===t?0:e.length-t-1},_valueMin:function(){return this.options.min},_valueMax:function(){return this.max},_refreshRange:function(e){"vertical"===e&&this.range.css({width:"",left:""}),"horizontal"===e&&this.range.css({height:"",bottom:""})},_refreshValue:function(){var t,i,e,s,a,n=this.options.range,h=this.options,l=this,u=!this._animateOff&&h.animate,r={};this._hasMultipleValues()?this.handles.each(function(e){i=(l.values(e)-l._valueMin())/(l._valueMax()-l._valueMin())*100,r["horizontal"===l.orientation?"left":"bottom"]=i+"%",o(this).stop(1,1)[u?"animate":"css"](r,h.animate),!0===l.options.range&&("horizontal"===l.orientation?(0===e&&l.range.stop(1,1)[u?"animate":"css"]({left:i+"%"},h.animate),1===e&&l.range[u?"animate":"css"]({width:i-t+"%"},{queue:!1,duration:h.animate})):(0===e&&l.range.stop(1,1)[u?"animate":"css"]({bottom:i+"%"},h.animate),1===e&&l.range[u?"animate":"css"]({height:i-t+"%"},{queue:!1,duration:h.animate}))),t=i}):(e=this.value(),s=this._valueMin(),a=this._valueMax(),i=a!==s?(e-s)/(a-s)*100:0,r["horizontal"===this.orientation?"left":"bottom"]=i+"%",this.handle.stop(1,1)[u?"animate":"css"](r,h.animate),"min"===n&&"horizontal"===this.orientation&&this.range.stop(1,1)[u?"animate":"css"]({width:i+"%"},h.animate),"max"===n&&"horizontal"===this.orientation&&this.range.stop(1,1)[u?"animate":"css"]({width:100-i+"%"},h.animate),"min"===n&&"vertical"===this.orientation&&this.range.stop(1,1)[u?"animate":"css"]({height:i+"%"},h.animate),"max"===n&&"vertical"===this.orientation&&this.range.stop(1,1)[u?"animate":"css"]({height:100-i+"%"},h.animate))},_handleEvents:{keydown:function(e){var t,i,s,a=o(e.target).data("ui-slider-handle-index");switch(e.keyCode){case o.ui.keyCode.HOME:case o.ui.keyCode.END:case o.ui.keyCode.PAGE_UP:case o.ui.keyCode.PAGE_DOWN:case o.ui.keyCode.UP:case o.ui.keyCode.RIGHT:case o.ui.keyCode.DOWN:case o.ui.keyCode.LEFT:if(e.preventDefault(),this._keySliding||(this._keySliding=!0,this._addClass(o(e.target),null,"ui-state-active"),!1!==this._start(e,a)))break;return}switch(s=this.options.step,t=i=this._hasMultipleValues()?this.values(a):this.value(),e.keyCode){case o.ui.keyCode.HOME:i=this._valueMin();break;case o.ui.keyCode.END:i=this._valueMax();break;case o.ui.keyCode.PAGE_UP:i=this._trimAlignValue(t+(this._valueMax()-this._valueMin())/this.numPages);break;case o.ui.keyCode.PAGE_DOWN:i=this._trimAlignValue(t-(this._valueMax()-this._valueMin())/this.numPages);break;case o.ui.keyCode.UP:case o.ui.keyCode.RIGHT:if(t===this._valueMax())return;i=this._trimAlignValue(t+s);break;case o.ui.keyCode.DOWN:case o.ui.keyCode.LEFT:if(t===this._valueMin())return;i=this._trimAlignValue(t-s)}this._slide(e,a,i)},keyup:function(e){var t=o(e.target).data("ui-slider-handle-index");this._keySliding&&(this._keySliding=!1,this._stop(e,t),this._change(e,t),this._removeClass(o(e.target),null,"ui-state-active"))}}})});
;!function(){document.addEventListener("DOMContentLoaded",function(){var a=document.getElementById("site-navigation");if(a){var b=a.querySelector("button");if(b){var c=a.querySelector("ul");if(!c)return void(b.style.display="none");b.setAttribute("aria-expanded","false"),c.setAttribute("aria-expanded","false"),c.classList.add("nav-menu"),b.addEventListener("click",function(){a.classList.toggle("toggled");var d=a.classList.contains("toggled")?"true":"false";b.setAttribute("aria-expanded",d),c.setAttribute("aria-expanded",d)});var d=document.getElementsByClassName("handheld-navigation");d.length>0&&[].forEach.call(d[0].querySelectorAll(".menu-item-has-children > a, .page_item_has_children > a"),function(a){var b=document.createElement("button");b.setAttribute("aria-expanded","false"),b.classList.add("dropdown-toggle");var c=document.createElement("span");c.classList.add("screen-reader-text"),c.appendChild(document.createTextNode(storefrontScreenReaderText.expand)),b.appendChild(c),a.parentNode.insertBefore(b,a.nextSibling),a.parentNode.classList.contains("current-menu-ancestor")&&(b.setAttribute("aria-expanded","true"),b.classList.add("toggled-on"),b.nextElementSibling.classList.add("toggled-on")),b.addEventListener("click",function(){for(b.classList.toggle("toggled-on");c.firstChild;)c.removeChild(c.firstChild);var a=b.classList.contains("toggled-on");b.setAttribute("aria-expanded",a),c.appendChild(document.createTextNode(a?storefrontScreenReaderText.collapse:storefrontScreenReaderText.expand)),b.nextElementSibling.classList.toggle("toggled-on")})}),[].forEach.call(document.querySelectorAll(".storefront-handheld-footer-bar .search > a"),function(a){a.addEventListener("click",function(b){a.parentElement.classList.toggle("active"),b.preventDefault()})});var e=document.getElementsByClassName("storefront-handheld-footer-bar"),f=document.forms,g=function(a){return function(){a?document.body.classList.add("sf-input-focused"):document.body.classList.remove("sf-input-focused")}};if(e.length&&f.length)for(var h=0;h<f.length;h++)e[0].contains(f[h])||(f[h].addEventListener("focus",g(!0),!0),f[h].addEventListener("blur",g(!1),!0));if([].forEach.call(document.querySelectorAll(".site-header .menu-item > a, .site-header .page_item > a, .site-header-cart a"),function(a){a.addEventListener("focus",function(){var b=document.querySelectorAll(".focus");[].forEach.call(b,function(b){b.contains(a)||(b.classList.remove("focus"),b.firstChild&&b.firstChild.classList&&b.firstChild.classList.remove("blocked"))}),a.parentNode.classList.add("focus")})}),("ontouchstart"in window||navigator.maxTouchPoints)&&window.innerWidth>767){[].forEach.call(document.querySelectorAll(".site-header ul ul, .site-header-cart .widget_shopping_cart"),function(a){a.classList.add("sub-menu--is-touch-device")});var i=!1;[].forEach.call(document.querySelectorAll(".site-header .menu-item > a, .site-header .page_item > a, .site-header-cart a"),function(a){a.addEventListener("click",function(b){a.classList.contains("blocked")&&!1===i&&b.preventDefault(),i=!1}),a.addEventListener("pointerup",function(b){a.classList.contains("blocked")||"mouse"===b.pointerType?i=!0:"cart-contents"===a.className&&a.parentNode.nextElementSibling&&""!==a.parentNode.nextElementSibling.textContent.trim()||a.nextElementSibling?a.classList.add("blocked"):i=!0})}),[].forEach.call(document.querySelectorAll("body #page > :not( .site-header )"),function(a){a.addEventListener("click",function(){[].forEach.call(document.querySelectorAll(".focus, .blocked"),function(a){a.classList.remove("focus"),a.classList.remove("blocked")})})})}}}})}();
;!function(){var a=navigator.userAgent.toLowerCase().indexOf("webkit")>-1,b=navigator.userAgent.toLowerCase().indexOf("opera")>-1,c=navigator.userAgent.toLowerCase().indexOf("msie")>-1;(a||b||c)&&document.getElementById&&window.addEventListener&&window.addEventListener("hashchange",function(){var a=document.getElementById(location.hash.substring(1));a&&(/^(?:a|select|input|button|textarea)$/i.test(a.tagName)||(a.tabIndex=-1),a.focus())},!1)}();
;/*!
 * PEP v0.4.3 | https://github.com/jquery/PEP
 * Copyright jQuery Foundation and other contributors | http://jquery.org/license
 */
!function(a,b){"object"==typeof exports&&"undefined"!=typeof module?module.exports=b():"function"==typeof define&&define.amd?define(b):a.PointerEventsPolyfill=b()}(this,function(){"use strict";function a(a,b){b=b||Object.create(null);var c=document.createEvent("Event");c.initEvent(a,b.bubbles||!1,b.cancelable||!1);
// define inherited MouseEvent properties
// skip bubbles and cancelable since they're set above in initEvent()
for(var d,e=2;e<m.length;e++)d=m[e],c[d]=b[d]||n[e];c.buttons=b.buttons||0;
// Spec requires that pointers without pressure specified use 0.5 for down
// state and 0 for up state.
var f=0;
// add x/y properties aliased to clientX/Y
// define the properties of the PointerEvent interface
return f=b.pressure&&c.buttons?b.pressure:c.buttons?.5:0,c.x=c.clientX,c.y=c.clientY,c.pointerId=b.pointerId||0,c.width=b.width||0,c.height=b.height||0,c.pressure=f,c.tiltX=b.tiltX||0,c.tiltY=b.tiltY||0,c.twist=b.twist||0,c.tangentialPressure=b.tangentialPressure||0,c.pointerType=b.pointerType||"",c.hwTimestamp=b.hwTimestamp||0,c.isPrimary=b.isPrimary||!1,c}function b(){this.array=[],this.size=0}function c(a,b,c,d){this.addCallback=a.bind(d),this.removeCallback=b.bind(d),this.changedCallback=c.bind(d),A&&(this.observer=new A(this.mutationWatcher.bind(this)))}function d(a){return"body /shadow-deep/ "+e(a)}function e(a){return'[touch-action="'+a+'"]'}function f(a){return"{ -ms-touch-action: "+a+"; touch-action: "+a+"; }"}function g(){if(F){D.forEach(function(a){String(a)===a?(E+=e(a)+f(a)+"\n",G&&(E+=d(a)+f(a)+"\n")):(E+=a.selectors.map(e)+f(a.rule)+"\n",G&&(E+=a.selectors.map(d)+f(a.rule)+"\n"))});var a=document.createElement("style");a.textContent=E,document.head.appendChild(a)}}function h(){
// only activate if this platform does not have pointer events
if(!window.PointerEvent){if(window.PointerEvent=a,window.navigator.msPointerEnabled){var b=window.navigator.msMaxTouchPoints;Object.defineProperty(window.navigator,"maxTouchPoints",{value:b,enumerable:!0}),u.registerSource("ms",_)}else Object.defineProperty(window.navigator,"maxTouchPoints",{value:0,enumerable:!0}),u.registerSource("mouse",N),void 0!==window.ontouchstart&&u.registerSource("touch",V);u.register(document)}}function i(a){if(!u.pointermap.has(a)){var b=new Error("InvalidPointerId");throw b.name="InvalidPointerId",b}}function j(a){for(var b=a.parentNode;b&&b!==a.ownerDocument;)b=b.parentNode;if(!b){var c=new Error("InvalidStateError");throw c.name="InvalidStateError",c}}function k(a){var b=u.pointermap.get(a);return 0!==b.buttons}function l(){window.Element&&!Element.prototype.setPointerCapture&&Object.defineProperties(Element.prototype,{setPointerCapture:{value:W},releasePointerCapture:{value:X},hasPointerCapture:{value:Y}})}/**
   * This is the constructor for new PointerEvents.
   *
   * New Pointer Events must be given a type, and an optional dictionary of
   * initialization properties.
   *
   * Due to certain platform requirements, events returned from the constructor
   * identify as MouseEvents.
   *
   * @constructor
   * @param {String} inType The type of the event to create.
   * @param {Object} [inDict] An optional dictionary of initial event properties.
   * @return {Event} A new PointerEvent of type `inType`, initialized with properties from `inDict`.
   */
var m=["bubbles","cancelable","view","detail","screenX","screenY","clientX","clientY","ctrlKey","altKey","shiftKey","metaKey","button","relatedTarget","pageX","pageY"],n=[!1,!1,null,null,0,0,0,0,!1,!1,!1,!1,0,null,0,0],o=window.Map&&window.Map.prototype.forEach,p=o?Map:b;b.prototype={set:function(a,b){return void 0===b?this["delete"](a):(this.has(a)||this.size++,void(this.array[a]=b))},has:function(a){return void 0!==this.array[a]},"delete":function(a){this.has(a)&&(delete this.array[a],this.size--)},get:function(a){return this.array[a]},clear:function(){this.array.length=0,this.size=0},
// return value, key, map
forEach:function(a,b){return this.array.forEach(function(c,d){a.call(b,c,d,this)},this)}};var q=[
// MouseEvent
"bubbles","cancelable","view","detail","screenX","screenY","clientX","clientY","ctrlKey","altKey","shiftKey","metaKey","button","relatedTarget",
// DOM Level 3
"buttons",
// PointerEvent
"pointerId","width","height","pressure","tiltX","tiltY","pointerType","hwTimestamp","isPrimary",
// event instance
"type","target","currentTarget","which","pageX","pageY","timeStamp"],r=[
// MouseEvent
!1,!1,null,null,0,0,0,0,!1,!1,!1,!1,0,null,
// DOM Level 3
0,
// PointerEvent
0,0,0,0,0,0,"",0,!1,
// event instance
"",null,null,0,0,0,0],s={pointerover:1,pointerout:1,pointerenter:1,pointerleave:1},t="undefined"!=typeof SVGElementInstance,u={pointermap:new p,eventMap:Object.create(null),captureInfo:Object.create(null),
// Scope objects for native events.
// This exists for ease of testing.
eventSources:Object.create(null),eventSourceList:[],/**
     * Add a new event source that will generate pointer events.
     *
     * `inSource` must contain an array of event names named `events`, and
     * functions with the names specified in the `events` array.
     * @param {string} name A name for the event source
     * @param {Object} source A new source of platform events.
     */
registerSource:function(a,b){var c=b,d=c.events;d&&(d.forEach(function(a){c[a]&&(this.eventMap[a]=c[a].bind(c))},this),this.eventSources[a]=c,this.eventSourceList.push(c))},register:function(a){for(var b,c=this.eventSourceList.length,d=0;d<c&&(b=this.eventSourceList[d]);d++)
// call eventsource register
b.register.call(b,a)},unregister:function(a){for(var b,c=this.eventSourceList.length,d=0;d<c&&(b=this.eventSourceList[d]);d++)
// call eventsource register
b.unregister.call(b,a)},contains:/*scope.external.contains || */function(a,b){try{return a.contains(b)}catch(c){
// most likely: https://bugzilla.mozilla.org/show_bug.cgi?id=208427
return!1}},
// EVENTS
down:function(a){a.bubbles=!0,this.fireEvent("pointerdown",a)},move:function(a){a.bubbles=!0,this.fireEvent("pointermove",a)},up:function(a){a.bubbles=!0,this.fireEvent("pointerup",a)},enter:function(a){a.bubbles=!1,this.fireEvent("pointerenter",a)},leave:function(a){a.bubbles=!1,this.fireEvent("pointerleave",a)},over:function(a){a.bubbles=!0,this.fireEvent("pointerover",a)},out:function(a){a.bubbles=!0,this.fireEvent("pointerout",a)},cancel:function(a){a.bubbles=!0,this.fireEvent("pointercancel",a)},leaveOut:function(a){this.out(a),this.propagate(a,this.leave,!1)},enterOver:function(a){this.over(a),this.propagate(a,this.enter,!0)},
// LISTENER LOGIC
eventHandler:function(a){
// This is used to prevent multiple dispatch of pointerevents from
// platform events. This can happen when two elements in different scopes
// are set up to create pointer events, which is relevant to Shadow DOM.
if(!a._handledByPE){var b=a.type,c=this.eventMap&&this.eventMap[b];c&&c(a),a._handledByPE=!0}},
// set up event listeners
listen:function(a,b){b.forEach(function(b){this.addEvent(a,b)},this)},
// remove event listeners
unlisten:function(a,b){b.forEach(function(b){this.removeEvent(a,b)},this)},addEvent:/*scope.external.addEvent || */function(a,b){a.addEventListener(b,this.boundHandler)},removeEvent:/*scope.external.removeEvent || */function(a,b){a.removeEventListener(b,this.boundHandler)},
// EVENT CREATION AND TRACKING
/**
     * Creates a new Event of type `inType`, based on the information in
     * `inEvent`.
     *
     * @param {string} inType A string representing the type of event to create
     * @param {Event} inEvent A platform event with a target
     * @return {Event} A PointerEvent of type `inType`
     */
makeEvent:function(b,c){
// relatedTarget must be null if pointer is captured
this.captureInfo[c.pointerId]&&(c.relatedTarget=null);var d=new a(b,c);return c.preventDefault&&(d.preventDefault=c.preventDefault),d._target=d._target||c.target,d},
// make and dispatch an event in one call
fireEvent:function(a,b){var c=this.makeEvent(a,b);return this.dispatchEvent(c)},/**
     * Returns a snapshot of inEvent, with writable properties.
     *
     * @param {Event} inEvent An event that contains properties to copy.
     * @return {Object} An object containing shallow copies of `inEvent`'s
     *    properties.
     */
cloneEvent:function(a){for(var b,c=Object.create(null),d=0;d<q.length;d++)b=q[d],c[b]=a[b]||r[d],
// Work around SVGInstanceElement shadow tree
// Return the <use> element that is represented by the instance for Safari, Chrome, IE.
// This is the behavior implemented by Firefox.
!t||"target"!==b&&"relatedTarget"!==b||c[b]instanceof SVGElementInstance&&(c[b]=c[b].correspondingUseElement);
// keep the semantics of preventDefault
return a.preventDefault&&(c.preventDefault=function(){a.preventDefault()}),c},getTarget:function(a){var b=this.captureInfo[a.pointerId];return b?a._target!==b&&a.type in s?void 0:b:a._target},propagate:function(a,b,c){
// Order of conditions due to document.contains() missing in IE.
for(var d=a.target,e=[];d!==document&&!d.contains(a.relatedTarget);)
// Touch: Do not propagate if node is detached.
if(e.push(d),d=d.parentNode,!d)return;c&&e.reverse(),e.forEach(function(c){a.target=c,b.call(this,a)},this)},setCapture:function(b,c,d){this.captureInfo[b]&&this.releaseCapture(b,d),this.captureInfo[b]=c,this.implicitRelease=this.releaseCapture.bind(this,b,d),document.addEventListener("pointerup",this.implicitRelease),document.addEventListener("pointercancel",this.implicitRelease);var e=new a("gotpointercapture");e.pointerId=b,e._target=c,d||this.asyncDispatchEvent(e)},releaseCapture:function(b,c){var d=this.captureInfo[b];if(d){this.captureInfo[b]=void 0,document.removeEventListener("pointerup",this.implicitRelease),document.removeEventListener("pointercancel",this.implicitRelease);var e=new a("lostpointercapture");e.pointerId=b,e._target=d,c||this.asyncDispatchEvent(e)}},/**
     * Dispatches the event to its target.
     *
     * @param {Event} inEvent The event to be dispatched.
     * @return {Boolean} True if an event handler returns true, false otherwise.
     */
dispatchEvent:/*scope.external.dispatchEvent || */function(a){var b=this.getTarget(a);if(b)return b.dispatchEvent(a)},asyncDispatchEvent:function(a){requestAnimationFrame(this.dispatchEvent.bind(this,a))}};u.boundHandler=u.eventHandler.bind(u);var v={shadow:function(a){if(a)return a.shadowRoot||a.webkitShadowRoot},canTarget:function(a){return a&&Boolean(a.elementFromPoint)},targetingShadow:function(a){var b=this.shadow(a);if(this.canTarget(b))return b},olderShadow:function(a){var b=a.olderShadowRoot;if(!b){var c=a.querySelector("shadow");c&&(b=c.olderShadowRoot)}return b},allShadows:function(a){for(var b=[],c=this.shadow(a);c;)b.push(c),c=this.olderShadow(c);return b},searchRoot:function(a,b,c){if(a){var d,e,f=a.elementFromPoint(b,c);for(
// is element a shadow host?
e=this.targetingShadow(f);e;){if(
// find the the element inside the shadow root
d=e.elementFromPoint(b,c)){
// shadowed element may contain a shadow root
var g=this.targetingShadow(d);return this.searchRoot(g,b,c)||d}
// check for older shadows
e=this.olderShadow(e)}
// light dom element is the target
return f}},owner:function(a){
// walk up until you hit the shadow root or document
for(var b=a;b.parentNode;)b=b.parentNode;
// the owner element is expected to be a Document or ShadowRoot
return b.nodeType!==Node.DOCUMENT_NODE&&b.nodeType!==Node.DOCUMENT_FRAGMENT_NODE&&(b=document),b},findTarget:function(a){var b=a.clientX,c=a.clientY,d=this.owner(a.target);
// if x, y is not in this root, fall back to document search
return d.elementFromPoint(b,c)||(d=document),this.searchRoot(d,b,c)}},w=Array.prototype.forEach.call.bind(Array.prototype.forEach),x=Array.prototype.map.call.bind(Array.prototype.map),y=Array.prototype.slice.call.bind(Array.prototype.slice),z=Array.prototype.filter.call.bind(Array.prototype.filter),A=window.MutationObserver||window.WebKitMutationObserver,B="[touch-action]",C={subtree:!0,childList:!0,attributes:!0,attributeOldValue:!0,attributeFilter:["touch-action"]};c.prototype={watchSubtree:function(a){
// Only watch scopes that can target find, as these are top-level.
// Otherwise we can see duplicate additions and removals that add noise.
//
// TODO(dfreedman): For some instances with ShadowDOMPolyfill, we can see
// a removal without an insertion when a node is redistributed among
// shadows. Since it all ends up correct in the document, watching only
// the document will yield the correct mutations to watch.
this.observer&&v.canTarget(a)&&this.observer.observe(a,C)},enableOnSubtree:function(a){this.watchSubtree(a),a===document&&"complete"!==document.readyState?this.installOnLoad():this.installNewSubtree(a)},installNewSubtree:function(a){w(this.findElements(a),this.addElement,this)},findElements:function(a){return a.querySelectorAll?a.querySelectorAll(B):[]},removeElement:function(a){this.removeCallback(a)},addElement:function(a){this.addCallback(a)},elementChanged:function(a,b){this.changedCallback(a,b)},concatLists:function(a,b){return a.concat(y(b))},
// register all touch-action = none nodes on document load
installOnLoad:function(){document.addEventListener("readystatechange",function(){"complete"===document.readyState&&this.installNewSubtree(document)}.bind(this))},isElement:function(a){return a.nodeType===Node.ELEMENT_NODE},flattenMutationTree:function(a){
// find children with touch-action
var b=x(a,this.findElements,this);
// flatten the list
// make sure the added nodes are accounted for
return b.push(z(a,this.isElement)),b.reduce(this.concatLists,[])},mutationWatcher:function(a){a.forEach(this.mutationHandler,this)},mutationHandler:function(a){if("childList"===a.type){var b=this.flattenMutationTree(a.addedNodes);b.forEach(this.addElement,this);var c=this.flattenMutationTree(a.removedNodes);c.forEach(this.removeElement,this)}else"attributes"===a.type&&this.elementChanged(a.target,a.oldValue)}};var D=["none","auto","pan-x","pan-y",{rule:"pan-x pan-y",selectors:["pan-x pan-y","pan-y pan-x"]}],E="",F=window.PointerEvent||window.MSPointerEvent,G=!window.ShadowDOMPolyfill&&document.head.createShadowRoot,H=u.pointermap,I=25,J=[1,4,2,8,16],K=!1;try{K=1===new MouseEvent("test",{buttons:1}).buttons}catch(L){}
// handler block for native mouse events
var M,N={POINTER_ID:1,POINTER_TYPE:"mouse",events:["mousedown","mousemove","mouseup","mouseover","mouseout"],register:function(a){u.listen(a,this.events)},unregister:function(a){u.unlisten(a,this.events)},lastTouches:[],
// collide with the global mouse listener
isEventSimulatedFromTouch:function(a){for(var b,c=this.lastTouches,d=a.clientX,e=a.clientY,f=0,g=c.length;f<g&&(b=c[f]);f++){
// simulated mouse events will be swallowed near a primary touchend
var h=Math.abs(d-b.x),i=Math.abs(e-b.y);if(h<=I&&i<=I)return!0}},prepareEvent:function(a){var b=u.cloneEvent(a),c=b.preventDefault;return b.preventDefault=function(){a.preventDefault(),c()},b.pointerId=this.POINTER_ID,b.isPrimary=!0,b.pointerType=this.POINTER_TYPE,b},prepareButtonsForMove:function(a,b){var c=H.get(this.POINTER_ID);
// Update buttons state after possible out-of-document mouseup.
0!==b.which&&c?a.buttons=c.buttons:a.buttons=0,b.buttons=a.buttons},mousedown:function(a){if(!this.isEventSimulatedFromTouch(a)){var b=H.get(this.POINTER_ID),c=this.prepareEvent(a);K||(c.buttons=J[c.button],b&&(c.buttons|=b.buttons),a.buttons=c.buttons),H.set(this.POINTER_ID,a),b&&0!==b.buttons?u.move(c):u.down(c)}},mousemove:function(a){if(!this.isEventSimulatedFromTouch(a)){var b=this.prepareEvent(a);K||this.prepareButtonsForMove(b,a),b.button=-1,H.set(this.POINTER_ID,a),u.move(b)}},mouseup:function(a){if(!this.isEventSimulatedFromTouch(a)){var b=H.get(this.POINTER_ID),c=this.prepareEvent(a);if(!K){var d=J[c.button];
// Produces wrong state of buttons in Browsers without `buttons` support
// when a mouse button that was pressed outside the document is released
// inside and other buttons are still pressed down.
c.buttons=b?b.buttons&~d:0,a.buttons=c.buttons}H.set(this.POINTER_ID,a),
// Support: Firefox <=44 only
// FF Ubuntu includes the lifted button in the `buttons` property on
// mouseup.
// https://bugzilla.mozilla.org/show_bug.cgi?id=1223366
c.buttons&=~J[c.button],0===c.buttons?u.up(c):u.move(c)}},mouseover:function(a){if(!this.isEventSimulatedFromTouch(a)){var b=this.prepareEvent(a);K||this.prepareButtonsForMove(b,a),b.button=-1,H.set(this.POINTER_ID,a),u.enterOver(b)}},mouseout:function(a){if(!this.isEventSimulatedFromTouch(a)){var b=this.prepareEvent(a);K||this.prepareButtonsForMove(b,a),b.button=-1,u.leaveOut(b)}},cancel:function(a){var b=this.prepareEvent(a);u.cancel(b),this.deactivateMouse()},deactivateMouse:function(){H["delete"](this.POINTER_ID)}},O=u.captureInfo,P=v.findTarget.bind(v),Q=v.allShadows.bind(v),R=u.pointermap,S=2500,T=200,U="touch-action",V={events:["touchstart","touchmove","touchend","touchcancel"],register:function(a){M.enableOnSubtree(a)},unregister:function(){},elementAdded:function(a){var b=a.getAttribute(U),c=this.touchActionToScrollType(b);c&&(a._scrollType=c,u.listen(a,this.events),
// set touch-action on shadows as well
Q(a).forEach(function(a){a._scrollType=c,u.listen(a,this.events)},this))},elementRemoved:function(a){a._scrollType=void 0,u.unlisten(a,this.events),
// remove touch-action from shadow
Q(a).forEach(function(a){a._scrollType=void 0,u.unlisten(a,this.events)},this)},elementChanged:function(a,b){var c=a.getAttribute(U),d=this.touchActionToScrollType(c),e=this.touchActionToScrollType(b);
// simply update scrollType if listeners are already established
d&&e?(a._scrollType=d,Q(a).forEach(function(a){a._scrollType=d},this)):e?this.elementRemoved(a):d&&this.elementAdded(a)},scrollTypes:{EMITTER:"none",XSCROLLER:"pan-x",YSCROLLER:"pan-y",SCROLLER:/^(?:pan-x pan-y)|(?:pan-y pan-x)|auto$/},touchActionToScrollType:function(a){var b=a,c=this.scrollTypes;return"none"===b?"none":b===c.XSCROLLER?"X":b===c.YSCROLLER?"Y":c.SCROLLER.exec(b)?"XY":void 0},POINTER_TYPE:"touch",firstTouch:null,isPrimaryTouch:function(a){return this.firstTouch===a.identifier},setPrimaryTouch:function(a){
// set primary touch if there no pointers, or the only pointer is the mouse
(0===R.size||1===R.size&&R.has(1))&&(this.firstTouch=a.identifier,this.firstXY={X:a.clientX,Y:a.clientY},this.scrolling=!1,this.cancelResetClickCount())},removePrimaryPointer:function(a){a.isPrimary&&(this.firstTouch=null,this.firstXY=null,this.resetClickCount())},clickCount:0,resetId:null,resetClickCount:function(){var a=function(){this.clickCount=0,this.resetId=null}.bind(this);this.resetId=setTimeout(a,T)},cancelResetClickCount:function(){this.resetId&&clearTimeout(this.resetId)},typeToButtons:function(a){var b=0;return"touchstart"!==a&&"touchmove"!==a||(b=1),b},touchToPointer:function(a){var b=this.currentTouchEvent,c=u.cloneEvent(a),d=c.pointerId=a.identifier+2;c.target=O[d]||P(c),c.bubbles=!0,c.cancelable=!0,c.detail=this.clickCount,c.button=0,c.buttons=this.typeToButtons(b.type),c.width=2*(a.radiusX||a.webkitRadiusX||0),c.height=2*(a.radiusY||a.webkitRadiusY||0),c.pressure=a.force||a.webkitForce||.5,c.isPrimary=this.isPrimaryTouch(a),c.pointerType=this.POINTER_TYPE,
// forward modifier keys
c.altKey=b.altKey,c.ctrlKey=b.ctrlKey,c.metaKey=b.metaKey,c.shiftKey=b.shiftKey;
// forward touch preventDefaults
var e=this;return c.preventDefault=function(){e.scrolling=!1,e.firstXY=null,b.preventDefault()},c},processTouches:function(a,b){var c=a.changedTouches;this.currentTouchEvent=a;for(var d,e=0;e<c.length;e++)d=c[e],b.call(this,this.touchToPointer(d))},
// For single axis scrollers, determines whether the element should emit
// pointer events or behave as a scroller
shouldScroll:function(a){if(this.firstXY){var b,c=a.currentTarget._scrollType;if("none"===c)
// this element is a touch-action: none, should never scroll
b=!1;else if("XY"===c)
// this element should always scroll
b=!0;else{var d=a.changedTouches[0],e=c,f="Y"===c?"X":"Y",g=Math.abs(d["client"+e]-this.firstXY[e]),h=Math.abs(d["client"+f]-this.firstXY[f]);
// if delta in the scroll axis > delta other axis, scroll instead of
// making events
b=g>=h}return this.firstXY=null,b}},findTouch:function(a,b){for(var c,d=0,e=a.length;d<e&&(c=a[d]);d++)if(c.identifier===b)return!0},
// In some instances, a touchstart can happen without a touchend. This
// leaves the pointermap in a broken state.
// Therefore, on every touchstart, we remove the touches that did not fire a
// touchend event.
// To keep state globally consistent, we fire a
// pointercancel for this "abandoned" touch
vacuumTouches:function(a){var b=a.touches;
// pointermap.size should be < tl.length here, as the touchstart has not
// been processed yet.
if(R.size>=b.length){var c=[];R.forEach(function(a,d){
// Never remove pointerId == 1, which is mouse.
// Touch identifiers are 2 smaller than their pointerId, which is the
// index in pointermap.
if(1!==d&&!this.findTouch(b,d-2)){var e=a.out;c.push(e)}},this),c.forEach(this.cancelOut,this)}},touchstart:function(a){this.vacuumTouches(a),this.setPrimaryTouch(a.changedTouches[0]),this.dedupSynthMouse(a),this.scrolling||(this.clickCount++,this.processTouches(a,this.overDown))},overDown:function(a){R.set(a.pointerId,{target:a.target,out:a,outTarget:a.target}),u.enterOver(a),u.down(a)},touchmove:function(a){this.scrolling||(this.shouldScroll(a)?(this.scrolling=!0,this.touchcancel(a)):(a.preventDefault(),this.processTouches(a,this.moveOverOut)))},moveOverOut:function(a){var b=a,c=R.get(b.pointerId);
// a finger drifted off the screen, ignore it
if(c){var d=c.out,e=c.outTarget;u.move(b),d&&e!==b.target&&(d.relatedTarget=b.target,b.relatedTarget=e,
// recover from retargeting by shadow
d.target=e,b.target?(u.leaveOut(d),u.enterOver(b)):(
// clean up case when finger leaves the screen
b.target=e,b.relatedTarget=null,this.cancelOut(b))),c.out=b,c.outTarget=b.target}},touchend:function(a){this.dedupSynthMouse(a),this.processTouches(a,this.upOut)},upOut:function(a){this.scrolling||(u.up(a),u.leaveOut(a)),this.cleanUpPointer(a)},touchcancel:function(a){this.processTouches(a,this.cancelOut)},cancelOut:function(a){u.cancel(a),u.leaveOut(a),this.cleanUpPointer(a)},cleanUpPointer:function(a){R["delete"](a.pointerId),this.removePrimaryPointer(a)},
// prevent synth mouse events from creating pointer events
dedupSynthMouse:function(a){var b=N.lastTouches,c=a.changedTouches[0];
// only the primary finger will synth mouse events
if(this.isPrimaryTouch(c)){
// remember x/y of last touch
var d={x:c.clientX,y:c.clientY};b.push(d);var e=function(a,b){var c=a.indexOf(b);c>-1&&a.splice(c,1)}.bind(null,b,d);setTimeout(e,S)}}};M=new c(V.elementAdded,V.elementRemoved,V.elementChanged,V);var W,X,Y,Z=u.pointermap,$=window.MSPointerEvent&&"number"==typeof window.MSPointerEvent.MSPOINTER_TYPE_MOUSE,_={events:["MSPointerDown","MSPointerMove","MSPointerUp","MSPointerOut","MSPointerOver","MSPointerCancel","MSGotPointerCapture","MSLostPointerCapture"],register:function(a){u.listen(a,this.events)},unregister:function(a){u.unlisten(a,this.events)},POINTER_TYPES:["","unavailable","touch","pen","mouse"],prepareEvent:function(a){var b=a;return $&&(b=u.cloneEvent(a),b.pointerType=this.POINTER_TYPES[a.pointerType]),b},cleanup:function(a){Z["delete"](a)},MSPointerDown:function(a){Z.set(a.pointerId,a);var b=this.prepareEvent(a);u.down(b)},MSPointerMove:function(a){var b=this.prepareEvent(a);u.move(b)},MSPointerUp:function(a){var b=this.prepareEvent(a);u.up(b),this.cleanup(a.pointerId)},MSPointerOut:function(a){var b=this.prepareEvent(a);u.leaveOut(b)},MSPointerOver:function(a){var b=this.prepareEvent(a);u.enterOver(b)},MSPointerCancel:function(a){var b=this.prepareEvent(a);u.cancel(b),this.cleanup(a.pointerId)},MSLostPointerCapture:function(a){var b=u.makeEvent("lostpointercapture",a);u.dispatchEvent(b)},MSGotPointerCapture:function(a){var b=u.makeEvent("gotpointercapture",a);u.dispatchEvent(b)}},aa=window.navigator;aa.msPointerEnabled?(W=function(a){i(a),j(this),k(a)&&(u.setCapture(a,this,!0),this.msSetPointerCapture(a))},X=function(a){i(a),u.releaseCapture(a,!0),this.msReleasePointerCapture(a)}):(W=function(a){i(a),j(this),k(a)&&u.setCapture(a,this)},X=function(a){i(a),u.releaseCapture(a)}),Y=function(a){return!!u.captureInfo[a]},g(),h(),l();var ba={dispatcher:u,Installer:c,PointerEvent:a,PointerMap:p,targetFinding:v};return ba});