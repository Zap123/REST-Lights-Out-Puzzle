//model
var Game = {
    start: function(x, y) {
        return m.request({
            method: "POST",
            url: "/start",
            data: {
                'x': x,
                'y': y
            }
        }).then(function(e) {
            Game.grid(e);
            Game.dim_x(e.size[0]);
            Game.dim_y(e.size[1]);
        });
    },
    move: function(x, y) {
        return m.request({
            method: "POST",
            url: "/move",
            data: {
                'x': x,
                'y': y
            }
        }).then(Game.grid);
    },
    grid: m.prop([]),
    dim_x: m.prop([]),
    dim_y: m.prop([])
};

var CellGame = {
    //controller
    controller: function() {
        Game.start(6, 6)
        return {
            grid: Game.grid,
            move: function(x, y) {
                Game.grid(Game.move(x, y))
            },
            submit: function() {
                Game.start(Game.dim_x(), Game.dim_y())
            },
            dim_x: Game.dim_x,
            dim_y: Game.dim_y,
        }
    },

    //view
    view: function(ctrl) {
        return m("div", {
                'id': 'game'
            }, [
                m("h1", "Click to play"),
                ctrl.grid().level.map(function(row, x) {
                    return m("div", {
                        'id': 'grid'
                    }, [
                        row.map(function(column, y) {
                            return m("z", {class: column.state ?'cellOn':'cellOff',
                                onclick: function() {
                                    ctrl.move(x, y)
                                }
                            }, column.state)
                        })
                    ])
                }),
            ],
            m("h3", "Is game over? " + ctrl.grid().endgame),
            m("form", {
                action: '#'
            }, [
                m("input", {
                    onchange: m.withAttr("value", ctrl.dim_x),
                    type: "number",
                    value: ctrl.dim_x()
                }),
                m("input", {
                    onchange: m.withAttr("value", ctrl.dim_y),
                    type: "number",
                    value: ctrl.dim_y()
                }),
                m("button", {
                    onclick: ctrl.submit
                }, "submit")
            ])
        );
    }
};


//initialize
m.mount(document.getElementById("cellgame"), CellGame);