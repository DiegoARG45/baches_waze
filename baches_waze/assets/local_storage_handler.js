function saveButtonState(buttonId, state) {
    localStorage.setItem(buttonId, state);
}

function loadButtonState(buttonId) {
    return localStorage.getItem(buttonId);
}

if (!window.dash_clientside) {
    window.dash_clientside = {};
}
window.dash_clientside.clientside = {
    update_button_style: function(n_clicks, id) {
        var button = document.getElementById(id);
        if (button) {
            var state = loadButtonState(id);
            if (state === 'clicked' || n_clicks) {
                button.style.backgroundColor = 'lightblue';
                saveButtonState(id, 'clicked');
            }
        }
        return window.dash_clientside.no_update;
    }
};

document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('button[id^="alert-button-"], button[id^="recent-event-button-"]');
    buttons.forEach(function(button) {
        var state = loadButtonState(button.id);
        if (state === 'clicked') {
            button.style.backgroundColor = 'lightblue';
        }
    });
});