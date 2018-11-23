Hypertext Labs LLC

Domain: hypertextlabs.co

(a) Stack 

Frontend: React, Apollo, Graphql
Backend: Django 
Database(s): Mysql, PostgreSQL v9.4 Neo4J(?), AWS S3

(B) Workflow

Version Control: Github

https://code.stdlib.com/ - stdlib API (FAAS)

Backend (API) Snippets 
(existing integration; stripe, sms) - buildout Podio Integration, + Metrc Testing + possibly partial(?) infrastructure 

https://bitsrc.io/ - Bit 
Frontend (components) Bit helps you organize your components, share them as a team and keep them synced in all your projects.
This environment enables you to use and develop components from other projects. For example, components written in typescript can be used and developed in a project written in flow-typed. It also lets Bit test and build your components in isolation, so you can know the exact state of every component.


Development Practices

This is an outline of development methodologies that ought to be taken up when building upon Hypertext Labs application architecture

Version Control: GitHub
master/Launch/Production branches

Added a dev, launch and prod branch. dev will be active devlopment, launch will be for stdlib FAAS API functions, prod will be the other which is pushed towards produciton live enviornment, and master will hold as the absolute code base.

Component snippets - React/node
API snippets - Django/GQL/Python

Snippets primarily live within Dev branch - API snippets often move to Launch, Production will move to more permanent server architecture

Workspace: VS Code, Python 3.7, React, autoDocs, DjangoSnippets *this is for consistency throughout the codebase

Development Timeline

(a) Setup Workspace - git repo (local and on GitHub), create branches, instantiate React + Django + GQL  stack

(b) Configure Bit Component management

(c) Configure code.stdlib cmd line tools + workspace for easy and efficient API prototyping and integration