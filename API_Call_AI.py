

import requests

import json


API_KEY = "YOUR API KEY HERE"

url = "https://api.ppq.ai/chat/completions"

prompt = """  

Take the role of an expert brand strategist and market researcher. 
Based on these reviews of the brand, identify what the name of the product should be. 
Once you look through all the reviews, think through what the most appropriate name of the product is based on our customers prefrences, how they use it, why they use and any other psychographic or demographic based ways you can. 

<objective> read through the reviews and suggest a name and tagline for this product</objective> 
<details> based on these reviews, how do the customers like the current name</details> 

Think through your answer and develop the best brand positioning 

The data is here:
Protects from thorns but not for harder use around the garden...,"I brought these to help clear my garden of brambles, etc. Yes they do protect from brambles (as specified) and were comfy to wear but after three days of digging and removing plants they wore through on the upper finger-tip & knuckle (weird, as the palm-leather is still A-OK as you can see in the photos). It looks like there is a weakness on the interface between the leather & the upper material. So if you need a harder working gardening glove that also protects from brambles then I would recommend the WORKMAXX gardening gloves with tougher parts. Yes they will be heavier but I didn't know what the quality/longevity of the NickyPicky glove was like until I used it."
Great but lack durability,I bought these in March !they are really comfortable but sadly already a hole in the finger tips. I would have thought at least a year out of them.
"Fits the bill, but neatly.","I have used the gloves once and they seemed to be robust and to fit the bill. I was surprised that they weren't a bigger fit, as I opted for a large. They were quite neat, but not too small as to be a problem. If you normally take large, you might want to consider an extra large."
A lot of moisture not drying easily,"they are nice and comfy but the sustain a lot of humidity, and takes forever to dry"
Good protection but...,"These offer good protection against thorns and so on, but I rarely use them because they are uncomfortable. They seem to have several sharp bits that feel like they are scratching my hands and fingers while in use. Also the yellow leather inside at the finger tips is disintegrating and ends up in my fingernails. Not what you want from gloves that are supposed to help keep your hands clean!"
Small is big on the fingers,"Bit disappointed with these, brought two pairs of small, but on trying them, there is to much material in each finger, wasn't able to pick stuff up using them because of this. By no means are my hands tiny and I have long fingers, they fit on my hand but the fingers are too long, shame as they look like and feel of good quality."
Size,It says large but would hardly fit my 9 yr old daughter's hands.
Lovely material,"Really like the look and feel of these gloves. Unfortunately as there is no elastic or strap around the wrist, soil gets inside the gloves, which is very uncomfortable and means have to keep stopping what you're doing (planting etc), to remove the soil from inside the glove. If there was a Velcro wrist strap, then I would have given them 5 stars."
Too Wide,"These gloves are not suitable for women. The fingers and the palms are too wide.I only use them in the house for playing with my dog as I don’t want to touch his saliva-covered toys with my bare hands. Unlike lots of other leather gloves I’ve tried, they don’t let the moisture from the saliva seep through after extended use which makes them perfect for me. Another good thing is they don’t rip when someone accidentally catches my fingers, as well as his toy, between his teeth and he yanks on them - actually, this is where wide fingers come in handy, as it’s the gloves between his teeth, not my actual digit. His teeth, so far, have not pierced the leather. If the hands were only more fitting I could happily use them in the garden.Another good point: if you get an itch on your nose or perspiration on your upper lip, the suede on the back of the gloves is perfect for taking care of it."
Only partially thorn-resistant,Not fully resistant to bramble horns. B&Q white leather gloves were better. This leather is quite soft.
Lined,"This is not lined, but product information, say yes,,,?"
Build Quilty,Would have liked the leather lined with fabric on the inside or a good lining. The leather had a very strong die used in the colour and the VOC on this was a concern yellow die to strong. Would have taken untreated leather due to the chemical smell. VOC was less after 28 days. Concern on the Chemical die
Not brilliant,They do not last only for very light gardening jobs
Good quality gloves,The XL was too small I had to send it back and there were no XXL so had to buy another make. The gloves is well made though.
Quality not up to standard,Gloves are ok but the stitching has come apart on one of the fingers and I can see this happening further so not impressed with the quality
"ok gloves, but pretty thin","bought these for camping, fires etc. they do a job but are pretty thin and not great for handling pots that,s been in the fire etc.. ok for processing wood"
ok..ish,feels nice but worn out quick.
Gloves Have a Strong Smell,These gloves were true to size and well made but the fabric has a very strong smell which stays on your hands all day. I threw them out after the first use.
Not terrible,I've used these for weeding and could feel spiky thistles though them. I would have expected a bit more protection for my fingers to be honest.
Faulty so had to return otherwise would of been a five star,Mine had a hole in top of left hand glove so had to return they look good otherwise 
Only lasted 4 months!,"When these gloves arrived my husband was really happy with them, lovely soft feel, really nice fit. However after only 4 months they have a hole in one of the fingers. Very disappointing as I have gardening gloves that have lasted for years! Such a shame as we really thought we had found a great durable pair of gloves."
Mediocre,"Yeah these are just OK - they fit alright for the sizes listed, but aren't double layered/finished on the inside and so not that comfortable to wear. I've had better gloves."
Seams inside the fingers are annoying,"They look well made on the outside and fitted ok, but there are very noticeable seams at the tips of the fingers inside, which haven’t been trimmed as much as they could have been and they were really rubbing against my fingertips, especially on the index fingers. I had to return them, it would soon be very irritating to wear"
Good but not fully thorn-proof and expensive.,"I have bought two pairs of these gloves and they have performed fairly well but I have several injuries from blackberry thorns, so be aware, thorn-proof might be more honestly described as some thorn resistance.I have since purchased two pairs of gardening gloves that are indistinguishable from these but at the same price as one pair here."
Not good,Terrible - badly made and HUGE . My hands are a size 7 ie small and these gloves must be a size 10 . Very inaccurate sizing. Straight in the charity bag.
Used once,"Very nice looking and comfy, however after the first use they were put in the cupboard for about a week til needed again, however this was not possible as they had gone totally moldy and stank, apparently this can happen if the tanning hasnt been properly done, but i have no idea about that."
They look good,No idea if they are good or not as yet . For gift for Christmas so let's wait and see. .delivery only took 3 days. He is using them...presume ok.
Comfy to wear.,Bought for my daughter and she loves them. They are very flexible
Don’t work with bramble,Was expecting to be able to pull sharp weeds and thorny bramble but you can’t with these gloves. I gave them a 3 because you can pick up the sharp ones after they have been cut you just can’t use force with them
Read the blurb,Thought they were lined as well
"Nice gloves, but they are not ‘small’","Ordered these in a ‘small’… they are not small. They fit my husband, who I would say has average sized men’s hands. So he has some new gardening gloves and I’ll remain project manager."
Beautiful gloves.,"These gloves are well made, easy to wear and very comfortable. BUT, they are supposed to be fleece lined, they are not!!! So maybe you need to change the description on what you are selling. Would buy again, but not as fleece lined."
Gloves gives off orange dye stains!,Unfortunately these gloves stained my hands orange like I’ve been tangoed! Nightmare to wash stains of my hand. Great shame as good gloves for gardening and maintenance but manufacturing standards needs to be addressed
Don't bother.,Stitching fell apart on first wearing.Waste of money
These are not thorn proof!,I was simply bringing some dead brambles from the back garden to the front and a thorn went through the glove and into my right palm.. Several trips to minor injuries unit and the Dr and antibiotics and an infected wound that almost spoilt a recent holiday and finally my palm is getting better approx 1 month later.. Not good..
Good gloves,"The gloves are very strong but given that i ordered the small ones they are a bit and suspect they are a ""mans small
Check size you need before ordering,"I ordered M size for my Male smallish hands.The ones that arrived were considerably too small and will be offered to my daughter, who hopefully has smaller hands than me, and I will buy from a local outlet where I can check the sizing before buying - which I should possibly have done.They certainly don't look 'thorn proof 'compared to gardening gloves I have previously bought and hopefully my daughter will give them a test run later in the year."
Dont buy,"Terrible, get wet and spikes go through"
Size too big,I ordered small size but way too big. I wish there is an XXS or XS size to choose. I will keep it as a gift instead.
Poor sizing,"I ordered a medium, based on the size guide shown in the description on Amazon. What I got was way too big. No labelling to say what size the glove was, so was I sent a large by mistake or is their sizing wrong? Maybe there's just one size? I have no clue. Had to return as didn't fit my hands properly and that would adversely affect dexterity. Not happy I now have to travel to town and spend money on parking, just to return them."
Good - but not thorn proof,"Well made and good fit , but not thorn proof , which you'll painfully find out.They'll suffice as ordinary gardening gloves now and I'll need try a pair that are."
Won't protect you from THORNS,"I was trying to pull some small plants by hand, off the soil but pricked my fingers instead and the thorns were not even that big"
Durability?,Comfy but a hole in a finger after 2 months of normal domestic use. Not satisfactory.
Gloves,The gloves were advertised as thorn proof. Started using them and they are not
Stains your hands yellow,Good thick gloves but don’t get wet or they will stain your hands yellow!
Nice material but...,"Nice and supple material but stitching already coming away, hoping I can restitch them"
Dog ate them,Unfortunately I was out of the house when the gloves arrived. When u got back I found that the dog had eaten them. Not HP
Not fleeced lined,It clearly says that these gloves are fleeced lined and they are not.Returned 😡😡😡
Not thorn proof,"Comfortable but no way thorn proof, dissatisfied"
not as advertised,"Product does not have the fleece lining that is advertised, this means that other gloves are better priced.I purchased these gloves because of the advertised lining.This shortcoming is a pity because the gloves are well made."
Soaked right through almost immediately,Might be ok when dead-heading some roses or other light work. But not for handling wet stuff. Sopping wet in no time
Allergic reaction to chemicals,Caused a severe allergic reaction on my hands and stank of chemicals.
Sizing is off,I am female. I used the measurement chart to check sizes and ordered a small. They are huge. The fit my husband who has large man-hands! Sizing is totally off for females. Quality of glove is good - no complaint there.
Poor,"The inside of the glove is badly designed and very uncomfortable, especially when gripping something."
Rubbish do not buy dyed my hands yellow!,Dyed my hands yellow absolutely awful took days to get off ended up rubbing my hands with nail varnish remover
Not remotely 'thorn proof'!,"How these gloves are so highly rated and how they get away with saying that they're thorn proof is beyond me!They are well made, but they are absolutely NOT thorn proof!Try pulling Brambles or Rose bush clippings and you'll soon find out!They're not long lasting either.I've used mine only occasionally for very light gardening and they already have holes in the fingers."
Lasted barely two hours!,"I'm clearing brambles - so heavy duty work with a lot of thorns involved! The stitching round the thumbs was very badly done - just a few stitches when a few dozen are needed. Stitching came away within two hours, which was revealed by thumb getting thorned through a large hole. Gloves are now useless. My previous gloves lasted for decades. Definitely a case of buy cheap, buy twice."
Not for man hands,Small size
Not fleece lined,Ordered these as a stocking filler for my daughter only to find there is no fleece lining despite this being in the description. Having used these type of gloves in the past I wanted to avoid her having the yellow stains!
You need small hands,Quality is good but poor fit and I have only medium size hands
not thornproof at all,"Very disappointed with this product, got it specifically to handle bramble, they offered almost no protection at all"
Too big,I ordered the small. I don’t have particularly small hands but they were too big for me
Low quality and a poor fit.,As per title. Sent mine back.
Stitching gave way between fingers after 4 weeks light use,Used for light gardening - very disappointing
Poor quality - total waste of money,Don't waste your money - after wearing for the first time the material tore as it is so thin and of very poor quality.Unable to return as just outside the returns window period - bad experience all round
Wrong gloves!,Nice gloves- wrong size!! Sending back.
These gloves are not lined,"The description of the gloves on the web site says they are fleece lined. In reality, the gloves are not lined"
Untrue claim,"They have a cheek saying their gloves have a fleece lining. They don't, in fact they have no lining."
Not fleece lined,Description states the gloves are fleece lined. They are not. This aside the gloves are well made.
Already falling apart,"The return window for this product was 06/08, and I am writing this on 07,/08, so I am now stuck with a pair of defective gloves."
Reeks of chemicals,Absolutely horrid chemical smells. Would avoid at all costs.
Great Value,Excellent fit
Rubbish,cheap n nasty
still let a small thorn through,pruning still let a small thorn through
Ok,Ok but have had thorns of brambles go through the stitching
"Decent gloves, be careful with sizing and don’t expect a fleece lining to keep your hands warm","These are a decent pair of leather gardening gloves, which come up a little larger than I expected, though still wearable.The gloves are made really for larger mens hands rather than the generally smaller ladies Ines, but then a lot of gloves are made in that way. They are well stitched, the leather is decent and the split leather design is nicely presented with the more robust leather in the palms and lower fingers for durability.I do have one niggle though, and that’s that I expected them to be fleece lined as described, but the Ines I received weren’t. Not sure if I just got a errant pair? I was planning to use these for winter gardening projects, hence the fleece lining would have made them warmer. As it is because they are larger than expected I can wear them with inner gloves, but I was disappointed with that aspect.Overall decent gloves, be careful with sizing and don’t expect a fleece lining to keep your hands warm. Three stars from me."

Great Gloves !,"Quality product...Soft and good fit. 1st use on cutting back a pyracanthus, firethorn, total protection ... Excellent."
Best Protection I Have Found,I've wasted a small fortune on gardening gloves but at last a good pair! Tackled an out of control Kiftsgate (IYKYK) in Dads garden today and not one thorn got through . Very impressive gloves and not too bulky
Good quality and comfortable,"These are good gardening gloves. They don't stain, are comfortable to wear, and will protect your hands effectively when handling even sharp brambles. Happy with them, I buy a new pair once they're worn. Worth it."
Very good product,Very good protection for your hands - I have a lot of thorny plants in the garden and these gloves keep them all out. But they are supple enough to work in.Much better than fabric/synthetic gloves and for little extra money.
High quality gardening gloves,"Well made, comfortable, easy to use. They do come in quite large - I ordered medium and they are still quite big on me (normal glove size 7)."
Good garden gloves,I’ve only used it twice but it’s nice to use. Not too thin but not too thick that’s it’s hard to grasp tools or branches. My hands are size M (in Marigold) and these gloves are slightly big but not too big to fall off while using. Seams finished well. 
"Buy these, trust me",Great pair of gloves.I have the xlarge and would have preferred a larger pair but they fit. I pulled many weeds and handled some holly and not once did I get any prickle my fingers.I will buy another one when they wear out.I would recommend these gloves.Also they are well made and comfortable
Great set of gloves,Great gloves. Good price and nice fit. Seem to stop most brambles from getting through.
Very good,"Nettles? NopeThistles? NopeRose bushes? NopeNothing short of an ICBM is getting through these gloves lolGreat fit, decent dexterity, amazing protection"
Does the job,Rather big but should tackle the brambles
Brilliant. Buy them.,Never used gardening gloves before so always suffered from cuts and scratches. Now I have tried these I just can’t understand why I waited so long. They are bulletproof.
Useful a a bribe for unwilling helpers,"As an older woman I need a little help with heavier/tougher tasks in my garden. My grandson (age 27) is willing to help, but needs to protect his delicate hands when weeding or pruning or anything else really. So I bought these. They are manly and tough looking, they protect his hands from dirt and thorns and accidentially touching snails or worms. Unfortunately they do not protect me from his grumbles and toddler like behaviour. Would recommend."
Garden gloves.,Excellent tough wearing which I hope will last a long time. I bought XL size but I found that they were still a tight fit but no doubt will stretch after a bit of work.
Size up,Good quality and functioned well with regard to thorns but as an extra large I would say they were more large.
Great for a thorny isdue,Think so no thorns could hurt your fingers and still be able to flex your fingers like normal. Great for any thorny issue
Good enough for general harder gardening,Good enough for most general gardening - nettles not an issue and the majority of thorns.But occasionally the thorns get through.I'm a 9 or 10 glove and had the large and it fits well.Comfortable to ware and flexible enough not to give your hands an extra workout.
Good,All good 👍🏼
Hand protection,"Great gloves, really comfortable. Just what I needed to protect my hands whilst gardening. Will be buying another pair."
Garden gl,Very good
Good Gloves,Excellent gloves especially for the price. Surprisingly thorn resistant for the thickness. Enables good feel when using garden power tools as well.
Handy gloves,A useful pair of gloves for tackling bramble bushes etc👍
Great protection and comfortable to use,"Very happy with these gloves. Quick delivery. I have small hands so I ordered the small size. They are thick gloves. I used them as soon as arrived. They provide good grip and excellent protection from thorns, whilst being very comfortable to use. I've just ordered a pair for my husband in his size. Very pleased."
Good gardening gloves,Sturdy product delivered on time
Good protection from prickly plants.,Great protection against prickly bushes n plants. Hasn't pricked myself since I ordered them n worn them. Can get smelly after few minutes wearing them. But it's OK.
Top glove,Great value
Gardening gloves,They feel quite padded for dealing with anything prickly the quality is very good l purchased a medium pair they do seem a tad on a larger size
Great item perfect,"Great Item, does actually when I says in the item description"
Excellent quality and prevent thorn penetration,Excellent quality glove. Unlike the fabric gloves they stop thorn penetration and don't wear out. This is the second pair that I have bought for myself and I only needed a new pair because I abused the first pair when I used them while hand balling rubble for 2 days and put a small hole in one of the fingertips. So impressed I bought some as a gift for my father who is a keen gardener.
tough enough!,"used to clear brambles in overgrown garden, some thorns made it through but only just!. was comfortably grabbing the stems/stalks with very few penetrations. the ones that did go through were easy to pick out too"
Brilliant gloves,Brilliant gloves i bought a pair last year for work I've still got them but with a few holes so I bought again and when these wear out I'll buy the same again
Great quality,Great quality gloves. XL size just about fit my shovel sized hands
Gardening gloves,"These gloves have proved to be of excellent quality, giving assurance that the job in hand can be tackled in the safest way possible."
They fit like a glove!,they ARE thornproof
They work!,"Genuinely amazed by how these gardening gloves work. Pulling out nettles, bramble and rose thorns are no problem with these gloves. Ordered a second pair for a family member too!"
Great. But hole in the end of finger after heavy use.,3rd I've paid I've bought in about 9 months.They're great but I wear them out. Im a garden maintenance guy so they get abused.I really like them so accept that they get a hole in the end of the fingers after heave use.
"Very impressed, great quality for a good price","Very impressed, great quality for a good price. Allows me to handle a bramble bush without any worries or scratches"
Great gardening gloves,The fit is as stated. It is great to have heavy duty gardening gloves that are not too big for my hands. 
These gloves work.,"Used them to pull up thistles and nettles - no stings, no prickles. Very pleased"
All good,All good
Gardening gloves,"Great protection, used on heavy thorned rose bushes."
Gloves,Pretty good fit and good for those prickly bits
Great!,Perfect fit. Feels like my hands will be protected great value
Comfortable and protective.,Great gloves.
Hands,Very suitable for small hands
Measure carefully,These seem very good but I’m going to return them for a larger pair. I thought being an elderly lady with slim hands medium would do but they are much too small! Measure carefully !
Tough gloves,Good tough hard wearing gloves which have withstood bramble thorns.
Excellent,Excellent
you buy cheap you buy twice,"i have bought nicky picky before and they are excellent but a few weeks ago i saw the identical glove at £8.99 from a different seller instead of nicky picky at £9.99 so of course i bought the cheaper one. I made a mistake as the £1 cheaper glove was thin and inferior to nicky picky. thinking i was imaging it, i weighed the two different suppliers gloves and the £1 cheaper glove was only two thirds the weight of the nicky picky glove. Writing this i think i sound ridiculous .. but if it saves others from a wrong decision then i'll take the hit. Ive made the same mistake on amazon several times now - you live and learn (eventually)"
Highly recommend,"These gloves are very durable - I was picking up very prickly items in my garden and nothing came through, so my hands were very protected. I am not sure how long they will last but I’m very happy."
Great but lack durability,I bought these in March !they are really comfortable but sadly already a hole in the finger tips. I would have thought at least a year out of them.
Protects from thorns but not for harder use around the garden...,"I brought these to help clear my garden of brambles, etc. Yes they do protect from brambles (as specified) and were comfy to wear but after three days of digging and removing plants they wore through on the upper finger-tip & knuckle (weird, as the palm-leather is still A-OK as you can see in the photos). It looks like there is a weakness on the interface between the leather & the upper material. So if you need a harder working gardening glove that also protects from brambles then I would recommend the WORKMAXX gardening gloves with tougher parts. Yes they will be heavier but I didn't know what the quality/longevity of the NickyPicky glove was like until I used it."
Leather garden gloves,Really happy
Comfortable and good fit,Comfortable well fitting glovesLeather is thinner than usual but does the job
Gardening gloves,"These are nice gloves but are not totally bramble thorn proof. Would I recommend these gloves, yes."
Perfect fit for men with small hands,Bought for a keen gardener who is out most days tending his garden and greenhouse. He seemed very pleased with them.
Good value,As discribed good quality and thorn proof
Amazing value,These gloves are made very well from a soft supple leather. They represent excellent value for money. Very durable and protective.
"Fits the bill, but neatly.","I have used the gloves once and they seemed to be robust and to fit the bill. I was surprised that they weren't a bigger fit, as I opted for a large. They were quite neat, but not too small as to be a problem. If you normally take large, you might want to consider an extra large."
Satisfied,Came up to expectation.
Happy,Great quality
Great gloves,Tough great fitting gloves.
Excellent,Great sturdy gloves - worth the money.
Good quality gardening gloves,"Great gloves, protect you from most thorns, brambles and nettles."
Very good protection from sharp objects. Comfy & well-fitting,"I really put these gloves through their paces doing a mix of gardening clearance and demolition of a shed and decking that have seen many better days. These gloves have saved me a LOT of times from getting screws and nails and other sharps in my hands. I find them very comfy, highly protective and I have ordered more - for a tenner these are worth every penny."
Comfortable to wear,"Very comfy and am able to work with them on, some leather gloves are so stiff it's impossible to hold anything with them on. Very pleased with these."
Great gloves,Great gloves for dealing with stinging nettles
Hard wearing,Perfect for the heavy garden work I had planned. Pulling brambles and weeding. Highly recommend
Good quality,Ideal for working with sharp Brambles
Best gloves ever,Truly thorn proof
Durable gloves,Great durable and tough gardening gloves
PLEASED,GOOD QUALITY PAIR OF GOODS. NOT THOROUGHLY TESTED YET
Thornproof,Bought these to tackle a large area of brambles.Excellent gloves with no thorn penetration.
Quality,Good quality robust gardening gloves
Very good fit,Very good fit and quality is exemplary
Great gloves,These are great. My garden is full of spiky plants and brambles. I've not been pierced once.
Gloves,Does job
Quality Gloves,Good quality and fit
Good protection,Good fit. Sturdy
Perfect,"Best value for money gloves , strong and durable!"
Soft and strong,My daughter asked me to get her these gloves as she is a gardener and finds they are so strong and long lasting
VERY GOOD GLOVES,Quite pleased with this purchase as they are comfortable to wear and well made. They are not thorn proof (what gloves are) but they serve their purpose. I have a pyracanth hedge with think long thorns but if I am careful and do not grasp anything to hard the thorns do not come through.Overall I would definitely recommend these gloves for gardening and any industrial work in the garden.
Excellent,Delivered promptly. No yellow hands! Fantastic. Nice soft leather and suede. Good fit.
Perfect for prickly roses,Bought these for my husband who was dealing with very prickly roses. He was delighted with them and assured me that not a prickle managed to pierce the gloves! Fantastic.
Good quality,Good solid gloves very comfortable and suitable for lifting or gardening work not sure if they will stop thorns etc from getting through as not used them yet but definitely good quality
I can't believe it actually works!,"I bought this pair of gloves because I had an upcoming job that required removing alot of brambles. On arrival, I doubted their ability to withstand puncture, as the material is thin and they are quite lightweight. Nevertheless I proceeded to use them. On the day, I was pleasantly surprised that no thorns were able to penetrate the gloves even with vigorous usage!"
"Do the job, maybe go a smaller size than normal though!","Do the job and good protection from thorns and sharp objects. Slightly on the big size compared to others I’ve bought previously. Apart from that, Would definitely recommend."
"Sturdy glove, good prickle protection","Sturdy gloves,the only gardening gl9ves I buy now"
Gardening gloves,Excellent gloves
They are thorn proof,They’re excellent gardening gloves and i would recommend them to anyone
Leather product,Excellent product
"Sturdy glove, good prickle protection","Sturdy gloves,the only gardening gl9ves I buy now"
A genuine product that actually does what it should do!,"Damned good gloves that actually work, lovely bit of leather!"
Gardening gloves.,"Love these gloves and they feel so nice on. Will save my hands from being constantly stabbed by my Pyracanthas. The best gardening gloves I have ever bought and good protection over arthritic hands. Not just for men, these fit me perfectly"
Happy with my purchase,"Very comfortable and I’m sure they will protect my hands against brambles I need to remove , I would consider I have medium size hands but ordered large and the are just fine for me"
Love them,Haven't used these much yet but they are lovely. Comfortable and they fit too. Stood up to some pretty lethal brambles
No more thorns in my fingers !,Definitely hard wearing and thornproof - as I deal with many rose types in my garden- absolutely invaluable and i thoroughly recommend!
Great Gardening Gloves,"Tried some cheap gardening gloves, which probed a false economy. These are more robust and have been great so it’s definitely worth paying a little more."
"Swift delivery, good quality and fit. Ideal for my purpose.",Exactly as described. Thank you.
Great gloves,Love these ans even better the thorns don't nick your fingers
Tough,Clearing brambles and not a single thorn made it through to my hand
"""

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}



data = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    
}

response = requests.post(url, headers=headers, json=data)
output = response.json()

print(output)

print("Data saved to output.json")
