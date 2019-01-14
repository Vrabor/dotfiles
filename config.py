from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, Key, Screen
import os
import subprocess

wmname = 'qtile'
mod = 'mod4'

# Key bindings
keys = [
    # Window manager controls
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod], 'r', lazy.spawncmd()),
    Key([mod], 'Return', lazy.spawn('rxvt-unicode')),
    Key([mod], 'w',      lazy.window.kill()),

    Key([mod], 'Tab', lazy.layout.next()),
    Key([mod], 'Left', lazy.screen.prevgroup()),
    Key([mod], 'Right', lazy.screen.nextgroup()),

    # Layout modification
    Key([mod, 'control'], 'space', lazy.window.toggle_floating()),

    # Switch between windows in current stack pane
    Key([mod], 'k', lazy.layout.down()),
    Key([mod], 'j', lazy.layout.up()),

    # Move windows up or down in current stack
    #Key([mod, 'control'], 'k', lazy.layout.shuffle_down()),
    #Key([mod, 'control'], 'j', lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], 'space', lazy.layout.next()),
    
    # Toggle between different layouts as defined below
    Key([mod], 'Tab',    lazy.nextlayout()),

    #user defined
    Key([mod], '1', lazy.spawn("firefox")),
    Key([mod], '3', lazy.spawn("Ranger")),

    
    #Layouts
    #Xmonad
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'l', lazy.layout.right()),
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod, 'shift'], 'h', lazy.layout.swap_left()),
    Key([mod, 'shift'], 'l', lazy.layout.swap_right()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),
    Key([mod], 'i', lazy.layout.grow()),
    Key([mod], 'm', lazy.layout.shrink()),
    Key([mod], 'n', lazy.layout.normalize()),
    Key([mod], 'o', lazy.layout.maximize()),
    Key([mod, 'shift'], 'space', lazy.layout.flip()),

    #Bsp
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    Key([mod, 'shift'], 'Down', lazy.layout.flip_down()),
    Key([mod, 'shift'], 'Up', lazy.layout.flip_up()),
    Key([mod, 'shift'], 'Left', lazy.layout.flip_left()),
    Key([mod, 'shift'], 'Right', lazy.layout.flip_right()),
    Key([mod, 'control'], 'j', lazy.layout.grow_down()),
    Key([mod, 'control'], 'k', lazy.layout.grow_up()),
    Key([mod, 'control'], 'h', lazy.layout.grow_left()),
    Key([mod, 'control'], 'l', lazy.layout.grow_right()),
    Key([mod], 'n', lazy.layout.normalize()),
    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split()),

]

# Mouse bindings and options
mouse = (
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
)

bring_front_click = True
cursor_warp = False
follow_mouse_focus = True

# Groups
groups = [
    Group('a'),
    Group('s'),
    Group('d'),
    Group('f'),
]
for i in groups:
    # mod + letter of group = switch to group
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))

    # mod + shift + letter of group = switch to & move focused window to group
    keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))

dgroups_key_binder = None
dgroups_app_rules = []

# Layouts
layouts = [
    layout.MonadTall(margin = 10, border_focus = '#330033'),
]

# Screens and widget options
screens = [Screen(top = bar.Bar([
        # This is a list of our virtual desktops.
        widget.GroupBox(urgent_alert_method='text',
                        fontsize=10, 
                        borderwidth=1),
        # Current window name.
        widget.WindowName(foreground = "a0a0a0",),
        #widget.Wallpaper(),
        widget.Notify(),
        #widget.Wlan(), breaks config :( fix later
        widget.Volume(foreground = "70ff70"),
        widget.Clock(foreground = "a0a0a0",
                    fmt = '%Y-%m-%d %a %I:%M %p'),
        #widget.CurrentLayoutIcon(),
    ], 22)) # our bar is (xx)px high
]

widget_defaults = dict(
    font='Ubuntu',
    fontsize=15,
)

auto_fullscreen = True
