getSiblings = function (elem) {
    var siblings = [];
    var sibling = elem.parentNode.firstChild;
    for ( ; sibling; sibling = sibling.nextSibling ) {
        if ( sibling.nodeType === 1 && sibling !== elem ) {
            siblings.push( sibling );
        }
    }
    return siblings;
};

var Gallery = function() {
  
  var
    gallery,
    slides;

  var _init = function() {
    gallery = document.getElementsByClassName('gallery')[0];
    slides = document.getElementsByClassName('gallery__item');
    slides = Array.prototype.slice.call( slides, 0 );
    _setPerspective();
    _eventHandler();
    _animateIn();
  }
  
  var _animateIn = function() {
    
    TweenMax.staggerFrom(slides, 0.4, {opacity: 0, rotationY:-90, transformOrigin:'left -200px 50% ', delay:0.5}, 0.3)
  }
  
  var _setPerspective = function() {
		 TweenLite.set(slides, {perspective:-400, visibility:'visible'});  
	}
  
  var _eventHandler = function() {
    slides.forEach(function(element,index) {      
      element.addEventListener('mouseover', _animateSlideIn, false);
      element.addEventListener('mouseleave', _animateSlideOut, false);
    }, this);    
  }
  
  var _animateSlideIn = function() {    
    var siblings = getSiblings(this);  
    siblings.forEach(function(element, index) {      
      var title = element.children[1].children[0];
      TweenLite.set(title,{opacity: 0}, 0)        
    })
    var title = this.children[1].children[0];
    var tl = new TimelineLite();
    tl
      .set(title, {y:50, opacity: 0})
      .to(this, 0.3, {opacity:1, width:'36%', ease:Linear.easeNone})
      .to(title, 0.3, {y:0, autoAlpha:1})
      .to(siblings, 0.3, {width: '16%', ease:Linear.easeNone}, 0);
  }
  
  var _animateSlideOut = function() {
    var siblings = getSiblings(this);
    siblings.forEach(function(element, index) {
      var title = element.children[1].children[0];      
      TweenLite.set(title,{opacity: 0}, 0);      
    });
    var tl = new TimelineLite();
    var title = this.children[1].children[0];
    tl
      .to(this, 0.3, {width:'20%', opacity:0.5, ease:Linear.easeNone})
      .to(title, 0.3, {opacity:0}, 0)
      .to(siblings, 0.3, {width:'20%', ease:Linear.easeNone}, 0); 
  }
  
  var _animateOthers = function() {
   
  }
  
  return {
    init: _init
  }
}();

Gallery.init();