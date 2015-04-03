var SignupForm = React.createClass({
    cancel: function(e) {
        e.preventDefault();
        React.unmountComponentAtNode(this.props.element);
        $(this.props.element).remove();
    },

    render: function() {
        return (
            <div className="sign-up-form">
                <form method="post" action="/1/auth/users">
                    <div id="legend">
                        <legend>Sign up for extra time</legend>
                    </div>
                    <div className="form-group">
                        <label>Time</label>
                        <div><DayLabel date={this.props.date} /></div>
                        <div>Period {this.props.period} ({this.props.time})</div>
                    </div>
                    <div className="form-group">
                        <label>Instructor</label>
                        <input type="email" className="form-control" id="email" name="email"
                               placeholder="ex. Eden Gulledge" />
                    </div>
                    <div className="form-group">
                        <label>Class</label>
                        <input type="password" className="form-control" name="password"
                               id="password" placeholder="ex. Algebra 2" />
                    </div>
                    <button type="submit" className="btn btn-default">Submit</button>
                    <button className="btn btn-default" onClick={this.cancel}>Cancel</button>
                </form>
            </div>
        );
    }
});


var Period = React.createClass({
    get_sign_up_info: function() {
        $("<div id='sign-up-overlay'/>").prependTo("#content");

        var element = document.getElementById('sign-up-overlay');

        React.render(
            <SignupForm user={this.props.user} time={this.props.time}
                period={this.props.period} date={this.props.date}
                element={element} />,
            element
        )
    },

    render: function() {
        return (
            <tr>
                <td>{this.props.time}</td>
                <td>
                    {this.props.period}
                    <i className="sign-up-button glyphicon glyphicon-pencil pull-right"
                        onClick={this.get_sign_up_info}></i>
                </td>
            </tr>
        );
    }
});


var PeriodList = React.createClass({
    render: function() {
        var schedule = this.props.schedule || [],
            user = this.props.user,
            date = this.props.date;

        schedule = schedule.map(function(period) {
            return (
                <Period time={period[0]} period={period[1]}
                    user={user} date={date} />
            );
        });

        return (
            <table className="table table-striped">
                <tbody>
                    {schedule}
                </tbody>
            </table>
        )
    }
});


var NavButton = React.createClass({
    handleClick: function() {
        this.props.onNavigate(this.props.day);
    },

    render: function() {
        return (
            <a className="btn btn-default"
                onClick={this.handleClick}>{this.props.label}</a>
        )
    }
});


var SchoolButton = React.createClass({
    handleClick: function() {
        this.props.onSchoolClick(this.props.school);
    },

    render: function() {
        return (
            <a className="btn btn-default"
                onClick={this.handleClick}>{this.props.school.toUpperCase()}
            </a>
        )
    }
});


var DayLabel = React.createClass({
    render: function() {
        var date_label = this.props.date ?
            moment(this.props.date, 'YYYY-MM-DD').format('dddd, MMMM Do') : "";
        var day_label = this.props.day_type ? '—' + this.props.day_type : "";

        return (<span>{date_label}{day_label}</span>);
    }
});


var DaySchedule = React.createClass({
    getInitialState: function () {
        return {schedule: []};
    },

    loadSchedule: function (day, school) {
        var url = day ?
            "/1/schedule/" + day
            : this.props.url;

        school = school || this.state.school;
        url = [url, "?school=", school].join("");

        $.ajax({
            url: url,
            dataType: 'json',
            success: function (data) {
                this.setState(data);
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },

    changeSchool: function(currentSchool) {
        var school = currentSchool == 'us' ? 'ms' : 'us';
        this.loadSchedule(this.state.date, school);
    },

    componentDidMount: function () {
        this.loadSchedule();
    },

    componentDidUpdate: function() {
        this.renderLabel(this.state.date, this.state.day_type);
    },

    renderLabel: function(date, day_type) {
        React.render(
            <DayLabel date={date} day_type={day_type} />,
            document.getElementById('day-label')
        )
    },

    render: function () {
        return (
            <div>
                <PeriodList schedule={this.state.schedule} date={this.state.date}
                    user={this.state.user} />

                <br/>

                <div className="nav">
                    <NavButton label="« Previous" day={this.state.day_before}
                        onNavigate={this.loadSchedule} />
                    &nbsp;
                    <SchoolButton school={this.state.school || this.props.school}
                        onSchoolClick={this.changeSchool} />
                    &nbsp;
                    <NavButton label="Next »" day={this.state.day_after}
                        onNavigate={this.loadSchedule} />
                </div>
            </div>
        )
    }
});


React.render(
    <DaySchedule url={"/1/schedule/" + $(location).attr('hash').slice(1)}
        school={$.url.param('school') || 'us'} />,
    document.getElementById('content')
);
