unum/devs
============

This doc shows how to setup your machine (Mac only) to develop for Unifist. When finished, you'll be running the base code for an Unum locally, including having your own bot record your Discord activity. 

Right now, only know how to do on Mac/Linux. Happy to learn otherwise or work with folks but need things simple.

# accounts

You don't have to use your personal accounts for anything. These accounts are needed to join us in developing: And they all sould be free:

- [GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
  - [2FA](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)
  - [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Discord](https://support.discord.com/hc/en-us/articles/360033931551-Getting-Started)

# install

This sets up your Mac with all the required tools to run and Unum locally

Install on your Mac:
- Apple Xcode: https://developer.apple.com/xcode/
- Homebrew: https://brew.sh/
- VS Code: https://code.visualstudio.com/
- GitHub Desktop: https://desktop.github.com/download/
- Docker Desktop: https://docs.docker.com/desktop/
  - After you install
  - Go into Settings -> Kubernetes -> Enable Kubernetes
  - Restart Docker Desktop (it'll take awhoel for Kuberentes to be ready)
- kubectl - https://formulae.brew.sh/formula/kubernetes-cli
- kubectx - https://formulae.brew.sh/formula/kubectx
- Tilt - https://formulae.brew.sh/formula/tilt

# run

These are the steps to run an Unum locally

## mysql pillar

A Pillar in an Unum is software we didn't write or control at all but we use to support an Uunum.

This'll run MySQL in your local Docker Desktop, required by Apps and Origins.

- Check out the repo with GitHub Desktop
  - Url: https://github.com/unum-pillars/mysql
  - Path: /Users/(username)/Documents/GitHub/unum-pillars/mysql
    - We'll be doing lots of orgs, so put the org path in the checkout
- Open in VSCode: Cmd-Shift-A
- Open a terminal: Ctrl-~
- Start it up by typing `make up`
- Hit space to open Tilt
- Click on db to watch it start up
  - It'll do some stuff at first and then restart
  - You'll be using Tilt like this a lot

Open another terminal, connect locally and see what databases are there (use README)

## ledger app

An App in an Unum is software we write and control the backend/storage of. 

This'll run the base App, ledger in your local Docker Desktop. The Ledger of an Unum records Unums, Entities, Facts, what did happen, and Acts, what should happen, and the access controls thereof. 

- Check out the repo with GitHub Desktop
  - Url: https://github.com/unum-apps/ledger
  - Path: /Users/(username)/Documents/GitHub/unum-apps/ledger
- Open in VSCode: Cmd-Shift-A
- Open a terminal: Ctrl-~
- Start it up by typing `make up`
- Hit space to open Tilt
- Click on gui to watch it start up
- Create a few records
  - In Tilt, click the localhost link in gui
  - Create an Unum
    - Call it whatever you want
  - Create an Entity in that Unum
    - Be yourself!

## discord origin

An Origin in an Unum is software we write but don't control the backend/storage of. We interface to some outside service.

This'll run the Discord origin in your local Docker Desktop. This allows an Unum to interact with Discord through a Bot

- Check out the repo with GitHub Desktop
  - Url: https://github.com/unum-origins/discord
  - Path: /Users/(username)/Documents/GitHub/unum-origins/discord
- Open in VSCode: Cmd-Shift-A
- Open a terminal: Ctrl-~
- Create a blank Discord secret by typing `make secret`
- Fill the secret
  - Create an App/Bot at https://discord.com/developers/applications?new_application=true
  - Put the token in secret/discord.json
  - Invite the Bot to your Discord server
- Start it up by typing `make up`
- Hit space to open Tilt
- Click on daemon to watch it start up
- Get Bot to record you
  - Go back to Ledger's Tilt window
  - Click the localhost link in gui
  - Create the Discord Origin
    - Call it `discord`
  - Create a Witness
    - Set it to your entity
    - Set who to your Discord User ID
      - https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID
  - Type something in your Discord Server
  - Check Facts to see if it's there
    - Check daemon in this Tilt to see log messages