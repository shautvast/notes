Bureaucratic cognitive load

https://teotti.com/cognitive-overload-in-software-development/

 Focuses on the architectural aspect of it 
 Ie some applications contain different functions that are not clearly divided into modules

 For developers that have worked with it extensively that is not a problem but for new employees this increases the cognitive load. For them the application is just one big blob of stuff. After a while working with it patterns emerge. The landscape slowly becomes navigable. 
While this is ultimately inevitable, help in the form of clear borders and maps or signposts in or around the code are helpful. Microservices are natural borders, like modules or packages. 

All true and helpful but cognitive load is a bigger concept. 

Consider the increasing amount of stuff that some organizations impose upon us poor developers.

Suppose you work on a small microservice that you know well because it’s small in the number of both functions and actual lines of code. Its overall function within the larger organization is also clear. The architects have done their job well. 

Suppose you have to add a new function that interacts with a different service. It could for instance fetch some data that is then added to the output of your own api. This is a very common situation when working with micro services. 

In order to be able to fetch this data you need to be added to the known consumers of the remote api. Your organization has a nice thing called a marketplace where you can subscribe and upon approval from their side you are given a token that you will add to the request along with your identity to prove that you are entitled to this data. 

It’s the first time that you do this and the procedure is not yet clear to you but it seems simple enough. You try your changes in the test environment but disappointingly you only get an empty response. You ask your coworkers but they only make a vague reference to yet another procedure that you will have to go through. 

As it turns out the data that you are trying to fetch and make part of your api is a birthdate. Because that is personal data and your organization has to comply with GDPR, the legal department must at all times be able to report what software uses what personal data and for which purpose. 

This is at first not clear to you but you stumble through a maze of documentation gradually getting an idea of what is going on. In order to read the birth date, you look the item up in a database of data attributes that are maintained by the company. There is not one but five different mentions of a birth date, with slightly different metadata so which is the right one? You ask your coworker who was in the middle of some thing completely different causing to switch context. Together you come to an educated guess and fill out an excel sheet that you have to send to some email address that was mentioned somewhere and wait for a week before you are given permission. 

you drop the work that you did in the meantime. You run your test and lo and behold, it works! 
You commit the code and start a pipeline to get ready for a release to the production environment. 

However, it fails because it’s been a while since this application was deployed last and some library that it uses, has been marked vulnerable by the security department. There is a way to circumvent this by adding to a special list that is part of your application called a whitelist. In there you mention the libraries that are vulnerable, but are not yet patched. This mechanism will allow you to deploy your app until that library is finally patched and you upgrade its version and remove it from the whitelist. 

Ok, try again. The pipeline reaches the test and acceptance environments. Nice. You do your final  tests, create some screenshots of the results that you add in a wiki page. By now you have also merged from your branch to develop and the to master with the positive review from your team mates. Luckily they don’t bother you with all the tiny code nitpicks like at your previous assignment. Be sure that the master PR is also authorized by a security champion otherwise some manager will send you an email complaining that the release was not in accordance with the guidelines. Oh and were is that email in which they announced the upcoming freeze because of the shareholder meeting. Ah, not until another week. 

Is there a pattern emerging here? These are actual examples that I dealt with in the past year. 

And by the way, the production deployment failed! Why? Because that procedure related to GDPR accountability needed to be done separately for production and I failed to notice because I have procedure dyslexia.

This is not to rant or complain. Or maybe it is. The actual point that I’m trying to make is that the amount of stuff you need to know sometimes to make the simplest update can be daunting. It sets you up for failure and lack of sleep. 

And there is even a more insidious effect. You  learnt all the procedure and were eventually successful showing the birthdate of the custom in the consent page of your frontend but it took you much longer than anticipated. There was also a sprint change while you were waiting for approval for a week. The story wasn’t done and had to be dragged into the next sprint. More and more your estimates become higher. Work starts to pile up. 

Add to this that you are not the only one facing this situation. What if you had deployed your app on test but because of the unexpected downstream response your upstream consumers also ran into an error. They filed a ticket, which your product owner dismissed  at first because she wasn’t aware of your situation but after two days you happen to see the ticket, have an Aha Erlebnis and restore the production version to make sure your consumers won’t be bothering in the evening hours because they need to go live with their major upgrade. 

Widespread instability on the test environment is a real thing, and it’s thoroughly demotivating. 

Ah you say, you need contract testing. You need mocks. More automated testing. Less toil.

And my answer is:

YES YES YES

And then I go: OMG another bucket of work into the overflowing backlog. 
The business isn’t happy. Shifting timelines. 