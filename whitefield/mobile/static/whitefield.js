var SignupForm = React.createClass({
    render: function() {
        return (
            <div className="sign-up-form">
                <form method="post" action="/1/auth/users">
                    <div id="legend">
                        <legend>AEC Exam Sign Up</legend>
                    </div>
                    <div className="form-group">
                        <label>Time</label>
                        <div><DayLabel date={this.props.date} /></div>
                        <div>Period {this.props.period} ({this.props.time})</div>
                    </div>
                    <div className="form-group">
                        <label>Instructor</label>
                        <input type="email" className="form-control" name="email"
                               placeholder="ex. Eden Gulledge" />
                    </div>
                    <div className="form-group">
                        <label>Class</label>
                        <input type="text" className="form-control" name="password"
                               placeholder="ex. Algebra 2" />
                    </div>
                    <button type="submit" className="btn btn-default">Submit</button>
                    <span>&nbsp;</span>
                    <button type="button" className="btn btn-default"
                        onClick={this.props.on_cancel}>Cancel</button>
                </form>
            </div>
        );
    }
});


var Period = React.createClass({
    do_sign_up: function() {
        this.props.do_sign_up({
            time: this.props.time,
            period: this.props.period
        });
    },

    render: function() {
        var sign_up;

        if (this.props.user && this.props.available_for_sign_up) {
            sign_up = (
                <i className="sign-up-button glyphicon glyphicon-pencil pull-right"
                        onClick={this.do_sign_up}></i>
            );
        }

        return (
            <tr>
                <td>{this.props.time}</td>
                <td>
                    {this.props.period}
                    {sign_up}
                </td>
            </tr>
        );
    }
});


var PeriodList = React.createClass({
    render: function() {
        var schedule = this.props.schedule || [],
            props = this.props;

        schedule = schedule.map(function(period) {
            var allow_sign_up = props.available_for_sign_up
                                     .indexOf(period[1]) >= 0;

            return (
                <Period time={period[0]} period={period[1]}
                    user={props.user} available_for_sign_up={allow_sign_up}
                    do_sign_up={props.do_sign_up} />
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

    sign_up_for: function(timeslot) {
        this.setState({
            sign_up_for: timeslot
        });
    },

    render: function () {
        if (this.state.sign_up_for) {
            return (
                <SignupForm user={this.state.user} date={this.state.date}
                    time={this.state.sign_up_for.time}
                    period={this.state.sign_up_for.period}
                    on_cancel={function() { this.sign_up_for(); }.bind(this)} />
            );
        } else {
            return (
                <div>
                    <PeriodList schedule={this.state.schedule} date={this.state.date}
                        user={this.state.user} do_sign_up={this.sign_up_for}
                        available_for_sign_up={this.state.available_for_sign_up} />

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
            );
        }
    }
});


React.render(
    <DaySchedule url={"/1/schedule/" + $(location).attr('hash').slice(1)}
        school={$.url.param('school') || 'us'} />,
    document.getElementById('content')
);
