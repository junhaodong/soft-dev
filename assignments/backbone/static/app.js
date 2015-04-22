var DataView = Backbone.View.extend({
    el: "#data",
    template: _.template($("#data_template").html()),
    initialize: function(){
	this.render();
    },
    render: function(){
	var e = this.template(this.model.toJSON());
	this.$el.empty();
	this.$el.append(e);
	return this;
    }
});

var EditView = Backbone.View.extend({
    el: "#edit",
    template: _.template($("#edit_template").html()),
    events: {
	"click #up" : function(e) {
	    var r = this.model.get("rating");
	    r = parseInt(r);
	    r = r + 1;
	    this.model.set('rating',r);
	    this.render();
	},
	"click #down" : function(e) {
	    var r = this.model.get("rating");
	    r = parseInt(r);
	    r = r - 1;
	    this.model.set('rating',r);
	    this.render();
	},
	"click #edit" : function(e) {
	    var desc = newDesc.value;
	    console.log(desc); //
	    this.model.set('desc', desc);
	    this.render();
	}
    },
    view: null,
    initialize: function(options){
	_.extend(this, _.pick(options, "view"));
	this.render();
    },
    render: function(){
	var e = this.template(this.model.toJSON());
	this.$el.empty();
	this.$el.append(e);
	this.view.render();
	return this;
    }
});

var Place = Backbone.Model.extend({
    initialize: function() {
	this.on({"change":function() {
	    console.log("Changed"+this.toJSON());}});
    },
    defaults:{
	'name':'name goes here',
     	'rating':0,
	'desc':'review goes here'
    },
    validate:function(attrs,options){
	if (isNaN(attrs.rating))
	    return "Rating must be numeric";
    }
});

var p1 = new Place({name:"Ferry's", rating:7, desc:"fake terry's; long line in the afternoon; many kids"});
var dv1 = new DataView({model:p1});
var ev1 = new EditView({model:p1, view: dv1});
