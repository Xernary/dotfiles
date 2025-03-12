alias snvim="sudo -e"
alias svim="sudo -e"

if status is-interactive
    # Commands to run in interactive sessions can go here
    starship init fish | source 
    # neofetch
    fastfetch --config arch
end

# Disable welcome prompt
set -g fish_greeting

# Source custom environment variables
source $HOME/.config/fish/custom_env_vars.fish

