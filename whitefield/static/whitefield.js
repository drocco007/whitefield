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
            <table>
                {schedule}
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


var DaySchedule = React.createClass({
    getInitialState: function () {
        return {schedule: []};
    },
    loadSchedule: function (day) {
        var url = day ?
            "/1/schedule/" + day
            : this.props.url;

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
    componentDidMount: function () {
        this.loadSchedule();
    },

    render: function () {
        return (
            <div>
                <h2>{this.state.day}–{this.state.date}–{this.state.day_type}</h2>

                <PeriodList schedule={this.state.schedule} />

                <br/>

                <NavButton label="« Previous" day={this.state.day_before}
                    onNavigate={this.loadSchedule} />
                &nbsp;
                <NavButton label="Next »" day={this.state.day_after}
                    onNavigate={this.loadSchedule} />
            </div>
        )
    }
});


React.render(
    <DaySchedule url={"/1/schedule/" + $(location).attr('hash').slice(1)} />,
    document.getElementById('content')
);
