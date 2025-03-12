alias snvim="sudo -e"
alias svim="sudo -e"

if status is-interactive
    # Commands to run in interactive sessions can go here
    starship init fish | source 
    # neofetch
    fastfetch --config arch
end

# disable welcome prompt
set -g fish_greeting


