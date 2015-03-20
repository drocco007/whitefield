var Period = React.createClass({
    render: function() {
        return (
            <tr>
                <td>{this.props.time}</td>
                <td>{this.props.period}</td>
            </tr>
        );
    }
});


var PeriodList = React.createClass({
    render: function() {
        var schedule = this.props.schedule || [];

        schedule = schedule.map(function(period) {
            return (
                <Period time={period[0]} period={period[1]} />
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
            <button onClick={this.handleClick}>{this.props.label}</button>
        )
    }
});


var SchoolButton = React.createClass({
    handleClick: function() {
        this.props.onSchoolClick(this.props.school);
    },

    render: function() {
        return (
            <button onClick={this.handleClick}>{this.props.school.toUpperCase()}
            </button>
        )
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

    render: function () {
        var date_label = this.state.date ?
            moment(this.state.date, 'YYYY-MM-DD').format('dddd, MMMM Do') : "";
        var day_label = this.state.day_type ? '—' + this.state.day_type : "";


        return (
            <div>
                <h3>{date_label}{day_label}</h3>

                <PeriodList schedule={this.state.schedule} />

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
