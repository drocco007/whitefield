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
        var schedule = this.props.schedule.map(function(period) {
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


var DaySchedule = React.createClass({
    getInitialState: function () {
        return {data: {schedule: []}};
    },
    loadCommentsFromServer: function () {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            success: function (data) {
                this.setState({data: data});
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    handleCommentSubmit: function (comment) {
        // TODO: submit to the server and refresh the list
        var comments = this.state.data;
        var newComments = comments.concat([comment]);
        this.setState({data: newComments});
    },
    componentDidMount: function () {
        this.loadCommentsFromServer();
        // setInterval(this.loadCommentsFromServer, this.props.pollInterval);
    },
    render: function () {
        return (
            <div>
                <h2>{this.state.data.day}–{this.state.data.date}–{this.state.data.day_type}</h2>

                <PeriodList schedule={this.state.data.schedule} />
            </div>
        )
    }
});


React.render(
    <DaySchedule url="/1/schedule/" />,
    document.getElementById('content')
);
