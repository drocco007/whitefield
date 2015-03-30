var SignInOutControl = React.createClass({
    logout: function(e) {
        $(this.getDOMNode()).parents(".collapse").collapse("hide");

        $.get('/1/auth/logout', function() {
            this.props.onLogout();
        }.bind(this));
    },

    render: function() {
        if (this.props.full_name) {
            return (
                <li>
                    <a href="#" onClick={this.logout}>Sign out</a>
                </li>
            );
        } else {
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
    }
});


var ProfileControl = React.createClass({
    render: function() {
        var school = this.props.school || "";

        if (school) {
            school = ["(", school.toUpperCase(), ")"].join("");
        }

        if (this.props.full_name) {
            return (
                <li className="">
                    <a href="#">
                        <i className="glyphicon glyphicon-user"></i>&nbsp;
                        {this.props.full_name} {school}
                    </a>
                </li>
            );
        } else {
            return null;
        }
    }
});


var NavBar = React.createClass({
    getInitialState: function() {
        return {};
    },

    loadUser: function() {
        $.ajax({
            url: '/1/auth/users/current',
            dataType: 'json',
            success: function (data) {
                this.replaceState(data);
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
        return (
            <ul className="nav navbar-nav navbar-right">
                <ProfileControl full_name={this.state.full_name}
                    school={this.state.school} />
                <SignInOutControl full_name={this.state.full_name}
                    onLogout={this.loadUser} />
            </ul>
        );
    }
});


React.render(
    <NavBar />,
    document.getElementById('navbar')
);
