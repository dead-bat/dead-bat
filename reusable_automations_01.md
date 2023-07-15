# Building Reusable Automations
Part I: Design Considerations

*July 2023*

In this first installment of this series, we're going to look at design considerations that will exponentially amplify the value of automation solutions. Presently, decision makers in organizations around the world are beginning to discover automation as a tool for increasing efficiency and reducing cost of their operations. Consequently, automations are usually built to fill a specific, single niche purpose. As an automation engineer, my primary goal is always to ensure that my clients receive the solutions that best fit their needs. However, over the years, I've started to look at the bigger picture. I no longer build automation solutions with the sole intent of filling a niche purpose. Instead, I play a longer game: build automations so that I can reuse them for different clients and in different environments by changing configurations. 

I aim to make my automation solutions as "genericized" and "marketable" as possible. First and foremost, this saves me a great deal of effort on my part when I can repurpose an existing solution rather than having to develop a new one from scratch. It also benefits my clients: when a more efficient way of doing something becomes apparent, or I need to patch a bug, I only need to edit a single codebase and deploy it to all clients that are using that solution -- this translates to greater uptime, resilience, and reliability for clients. The rapid implementation afforded by turnkey solutions is also not a hard sell -- clients no longer need to wait weeks or months for a solution to go live; it takes a couple hours, tops, and they're up and running.

In this write up, we're going to explore some of the methodology and considerations that go into building these reusable solutions. I hope this helps you reclaim more of your own time and productivity, and improve your own offerings.

**{TOC}**

## Reconsider the Process

The first stage is identifying what you're *actually* automating. This is often taken as a given -- you're automating the process your client has requested. However, if you build a broader contextual understanding of the automation, and explore the actions of the automation in an abstract sense, you will quickly find that the process you're automating is often already more generic than it seems.

For instance, if someone requests an automation for scheduling at a tour company, the immediate scope is to create an automated scheduling system that allows bookings from a web resource to be created and modified in a company calendar that may also be modified by employees in real time. But if we examine the tasks and consider them more abstractly, we find that this automation is not _just_ relevant to a single company, a single industry, or specific third party applications. We need to be able to correlate calendar management across multiple sources of data -- we need to be able to retrieve existing scheduled events, create new ones, set boundaries for "open hours" and "padding" time, and so on. These are all things that _any_ scheduling tool must do. If you build the automation with this genericization at the forefront of the design, and later you have other clients seeking to automate scheduling of _any type_, you should be able to modify some configuration in this initial automation and apply it to the new scenarios with minimal effort **and** *without changing the codebase*. The value of avoiding the need to change the codebase on a client-to-client basis cannot be overstated.

## Naturalize Data

Your automations should not assume anything about the data they are receiving. Data models, then, need to be layered.
