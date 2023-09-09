# Fund RevNet Development

## Synopsis

Allocate $75k towards RevNet (Revenue Network) development across three checkpoints.

## Motivation

In principle, Juicebox allows anyone to bootstrap and operate a project over time with transparent guarantees and incentives, and to strike a balance between centralization and decentralization according to their needs.

In practice, Juicebox has proven highly effective for bootstrapping projects, but outside of JuiceboxDAO itself (and projects closely working with it), fewer projects have gone on to sustainably operate using it. Although many factors are likely at play, one possible explanation is that:

1. For projects ultimately aiming to operate in a centralized manner, the overhead of operating on Juicebox isn't worth it once the project has been funded. This makes sense – Juicebox's mechanisms are very useful for building trust while bootstrapping these projects, but once they are established, the risk of smart contract exploits, onboarding difficulties for new crypto users, ETH's volatility, and the burden of onchain management often lead these project owners to migrate to fiat banking or manually managing funds through a multisig. This is not due to Juicebox's shortcomings; rather, it is a byproduct of operating within the Ethereum ecosystem.[^1]
2. Projects ultimately aiming to operate in a decentralized manner typically want to avoid having a project owner at all. Even if ownership can decentralize over time (e.g. via a multisig), the burden of governance and operation through a single point of failure (the project NFT) can prove cumbersome.

This issue applies to almost all governing and operative frameworks on Ethereum – even with tools like Governor Bravo, governance frequently becomes burdensome, and funding allocations can fail to reflect community wishes. These and other issues lead to community apathy and disengagement.

RevNets[^2] pose a solution to this problem: if a project operates entirely according to pre-determined rules and incentives, governance is no longer necessary, and a community can focus on their actual objectives instead of worrying about self-governing.

## How RevNets Work

RevNets are built on top of and extend the Juicebox protocol. RevNets are Juicebox projects, and anyone can deploy one. Like Juicebox projects, anyone can pay a RevNet with ETH and mint its tokens. RevNets start out minting 1 token per ETH, or if they use USD accounting, 1 token per USD worth of ETH.

A RevNet's token issuance evolves over generations which last a pre-defined length of time (28 days, for example). Three parameters determine how its tokens are issued:

1. The **Entry Curve**. The cost to enter the network increases over time, incentivizing people to join sooner. The entry curve defines how much more expensive tokens become each generation. With a 5% entry curve, 5% fewer tokens are minted per ETH each generation.
2. The **Exit Curve**. Leaving the network (by burning tokens) reclaims some ETH from the network. The closer an exit curve is to 100%, the more ETH goes to the last participants to exit, and less ETH goes to the first participants to exit. This incentivizes participants to stay in the network longer. You can visualize and experiment with different exit curves [on Desmos](https://www.desmos.com/calculator/q9jwaefswq).
3. The **Boost**. For a pre-determined length of time (140 days, for example) after a RevNet's creation, a percentage of newly generated tokens are allocated to a specific address. This address could be a developer multisig, a staking rewards contract, an airdrop stockpile, or something else. When the boost period ends, this allocation drops to 0.

RevNet creators can optionally pre-mint a number of tokens for themselves at the time of the network's creation. **RevNets have no owner.** Once they are deployed, their parameters are locked in place. Funds can only leave the network when people exit.

## Why Use RevNets?

Some options offer more centralized control, which can be helpful for bootstrapping project development, but can lead to issues on the path to decentralization. Other options prioritize decentralization, which can make it difficult to get a project off the ground.

RevNets solve both of these problems: the network begins decentralized, but the boost can be used to incentivize bootstrapping efforts as needed. They also:

- Don't require governance.
- Treat all participants equally. [Devs, investors, and customers are all incentivized](https://jango.eth.limo/?id=3EB05292-0376-4B7D-AFCF-042B70673C3D) to participate in the growth of the network.
- Are impossible to rugpull.

As long as a network continues to grow, the amount of ETH that current participants can reclaim by exiting will continue to rise. The most a participant can lose is difference between the ETH they entered with and the amount of ETH they can get back by exiting at that time.

RevNets won't be the best model for starting a hardware store, or for fundraisers where the owners need to maintain control. But for experimental software projects, ownerless social media networks, or new protocols like Juicebox, it offers a completely new type of model – one that might be able to out-compete traditional ones.

RevNets are obviously experimental and there's no guarantee that this will work, but we think it's worth experimenting with.

## What We're Building

1. A fully-featured frontend for creating, joining, exiting, and exploring RevNets. So far, peacenode has been leading the designs on [Figma](https://www.figma.com/file/77qCG4RaG0T1qfDHpRS2zI/Retailismo) and Aeolian has begun implementing the [`revnet-app`](https://github.com/rev-net/revnet-app). A work-in-progress prototype is available on [revnet-app.vercel.app](https://revnet-app.vercel.app/net/1223).
2. A collection of Ethereum smart contracts to extend the Juicebox protocol, allowing anyone to create or interact with customized RevNets. Further contract development may include lockup or other helper contracts for managing boost allocations, or something else.

Rob from Open Esquire has been hanging around the Discord server and providing input – we'd like to secure his services in addressing RevNet's legal needs.

## Specification

1. In the cycle following this proposal's approval, send $25,000 USD worth of ETH to the RevNet multisig[^3] to fund ongoing development.
2. In the first cycle once both a production-ready frontend and the core RevNet contracts are deployed, send $25,000 USD worth of ETH to RevNet.
3. In the first cycle once $100,000 USD worth of ETH flows through RevNets (not including RevNet's own network), send $25,000 USD worth of ETH to RevNet.

These distributions should only be made with approval from at least 60% of the JuiceboxDAO multisig. The initial distribution will be sent to the RevNet multisig, but future distributions may be sent to the RevNet multisig, a Juicebox project, or a RevNet network as dictated by RevNet multisig signers. 

## Timeline

We're planning a four-week sprint to get the first version of a RevNet frontend out and to have contracts deployed, and to keep moving from there. If you're interested in helping out, join the [Retailism Discord server](https://discord.gg/6Zr7Rtv6Ea).

## Risks

1. We're building complex software. There's always a risk of exploits, and this is particularly true of smart contract development.
2. For a variety of reasons, people might not want to use RevNets for their projects.
3. RevNet's economic models are untested, and might not work well in practice.
4. Development may take much longer than expected – it's hard to accurately project development timelines.

## Further Reading

1. Jango, [Retailism](https://jango.eth.limo/?id=9E01E72C-6028-48B7-AD04-F25393307132).
2. Jango, [Modeling Retailism](https://jango.eth.limo/?id=B762F3CC-AEFE-4DE0-B08C-7C16400AF718).
3. Aeolian, [Retailism: a first look](https://aeolian.eth.limo/E6F9D1FE-DB20-450C-8F37-78C3870D1620/).

Also see Jango's [other posts on Retailism](https://jango.eth.limo/?tags=retailism).

[^1]: These issues might be mitigated somewhat with multi-asset support (ERC-20 terminals), simple fiat onboarding in protocol clients, OAuth wallet creation, and further progress in onchain management tools like Safe.
[^2]: RevNets are an implementation of [Retailism](https://jango.eth.limo/?id=9E01E72C-6028-48B7-AD04-F25393307132), an organizational model conceived of by Jango. See [`retailism-templates`](https://github.com/mejango/retailism-templates) for an example implementation.
[^3]: The RevNet multisig is on Ethereum mainnet: [`0x8Bc12fEf1f8EFe25fE96fb9B407c46159e82201C`](https://app.safe.global/home?safe=eth:0x8Bc12fEf1f8EFe25fE96fb9B407c46159e82201C).
