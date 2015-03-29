var SignInControl = React.createClass({
    render: function() {
        return (
            <li className="dropdown">
                <a href="#" className="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
                    <i className="glyphicon glyphicon-user"></i>
                    Sign in
                </a>

                <form className="dropdown-menu" action="/1/auth/login" method="post">
                    <div className="form-group">
                        <label htmlFor="email">Email address</label>
                        <input type="email" className="form-control" id="email"
                            name="email" placeholder="Email address" />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" className="form-control" id="password"
                            name="password" placeholder="Password" />
                    </div>
                    <button type="submit" className="btn btn-primary">Submit</button>
                    <a href="/register.html" className="col-xs-offset-2">Create new account</a>
                </form>
            </li>
        );
    }
});


var AuthControl = React.createClass({
    getInitialState: function() {
        return {};
    },

    loadUser: function() {
        $.ajax({
            url: '/1/auth/users/current',
            dataType: 'json',
            success: function (data) {
                this.setState(data);
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },

    componentDidMount: function () {
        this.loadUser();
    },

    render: function() {
        if (!this.state.full_name) {
            return (
                <SignInControl />
            );
        } else {
            // FIXME: figure out a way to make both React and Bootstrap happy…
            return (
                <div>
                    <li className="">
                        <a href="#">
                            <i className="glyphicon glyphicon-user"></i>&nbsp;
                            {this.state.full_name}
                        </a>
                    </li>
                    <li>
                        <a href="/1/auth/logout">Sign out</a>
                    </li>
                </div>
            );
        }
    }
});


var NavBar = React.createClass({
    render: function() {
        return (
            <ul className="nav navbar-nav navbar-right">
                <AuthControl />
            </ul>
        );
    }
});

React.render(
    <NavBar />,
    document.getElementById('navbar')
);
