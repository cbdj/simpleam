# simpleam, Simple AdMob
Simple AdMob support for monetizing your android projects made with python. Firstly was designed for pygame android applications, but I guess it can be used in other frameworks?
This "module" is inspired by [KivMob](https://github.com/MichaelStott/KivMob), so you should definitely check it out too.

Now I\`ll explain here the basic usage of this "module": </br>
**Take in mind, this module requires from you basic knowledge of p4a and buidozer. In case you dont understand something, you can check Google firebase docs or `example` folder.**

Modifications to buildozer.spec file:
- `requirements = jnius, ...`
- `android.permissions = INTERNET, ACCESS_NETWORK_STATE`
- `android.api = 30`
- `android.minapi = 21`
- `android.sdk = 24`
- `android.ndk = 19b`
- `android.gradle_dependencies = 'com.google.firebase:firebase-ads:10.2.0'`
- `p4a.branch = master`
- `android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713 (TEST app ID, in release use your own app ID)`

It's better to mention, that you dont actually need to download jnius on your pc. 
Buildozer can download it when building your app.

To use the module, you have to initialize mobile ads first. You can do it by this function:</br>
`simpleam.simpleam_init("Your AdMob ID")`</br>
Dont supply an argument, if you want to use TEST ID. This **APPLIES TO ALL ADMOB OBJECTS**

Now, you can actually create some objects. Let's create a banner:</br>
`banner = simpleam.Banner(ad_id=None, position="BOTTOM", size="SMART_BANNER")`

This will create a banner in the bottom part of the screen, with "smart" size, which will automatically pick the best banner size.</br>
Position should be a constant, representing a `layout.Gravity` class constant. For example, `"LEFT" = Gravity.LEFT`, `"CENTER" = Gravity.CENTER` etc.</br>
For more, check this [documentation](https://developer.android.com/reference/android/view/Gravity)

Banner size however, can be a constant or custom tuple (Which of course not always can be displayed. Use constant size)
SMART_BANNER would be the best, because it automatically scales depending on your device screen.
But if you want use other sizes, you can pass a (x, y) argument, or other [constants](https://developers.google.com/android/reference/com/google/android/gms/ads/AdSize)

*That's all cool and anything, but how do I display the banner itself?*

Firstly, you have to load an ad.</br>
`banner.load_ad()`</br>
All AdMob objects have this method, so it's quite similar. It basically creates an ad builder, which then requests an ad from google.</br>
**The loading itself takes time, so you have to plan how to use ads effectively**

You can also filter ad, by passing in a `dict` argument: </br>
```py
ad_filters = {"children": True, "family": True} 
#children - ad is designed for shildren. family - ad is designed for families. Quite simple.
banner.load_ad(ad_filters)
```

After loading an ad, you can actually display it.
Banner has a method to change it\`s visibility: </br>
```py
banner.set_visibility(True) 
#True - visible, False - invisible` 
``` 
And that's it! Congratulations on your first ad object!

The next ad object is `Interstitial`.
It's a fast ad that appears on the fullscreen. It's quite easy to setup.

```py
interstitial = simpleam.Interstitial(ad_id=None)
interstitial.load_ad(filters = {})
interstitial.show()
```

There are some differences:
1. Interstitial can take **2 AdMob IDs**. 1 - Image interstitial ID, and 2 - Video interstitial ID. Quite simple. Want video? Create interstitial with video ID. No? Create without.
2. Interstitial and Rewarded instead of `set_visibility()` method, have `show` method.
3. Interstitial and Rewarded also have `is_loaded()` method, which indicates, if your ad is loaded. Use it in needed situations.

And now the last thing, `Rewarded` ad.
It takes some code examples, but I couldnt say it's hard to understand. Let's start from the template:

```py
points = 0
rewarded = simplead.Rewarded(ad_id=None)

class Callback(simpleam.RewardedCallbacks):
"""Callback class, which takes events from rewarded video, and makes some manipulations. 
   As an example, it adds 50 points, if user fully watched the ad.
   It also indicates if ad is loaded, if it failed to load, if it's closed and etc."""
		
    def on_rewarded_loaded(self):
        print("SIMPLEAM: Ad is loaded!")

    def on_rewarded_opened(self):
        print("SIMPLEAM: Ad is opened!")

    def on_rewarded_started(self):
        print("SIMPLEAM: Ad is started!")

    def on_rewarded_closed(self):
        print("SIMPLEAM: Ad closed!")

    def on_rewarded_success(self, reward):
        points += 50
        print(f"SIMPLEAM: Ad succesfully ended!")

    def on_rewarded_left(self):
        print("SIMPLEAM: Ad left application!")

    def on_rewarded_load_fail(self, num):
        print("SIMPLEAM: Ad failed to load!")

rewarded.set_listener(Callbacks()) # Loads our listener in the rewarded ad class. Now we can load a video
rewarded.load_ad()

if rewarded.is_loaded():
	rewarded.show()
# I`ll be back in 10 seconds.
```

**Be careful, because sometimes ad can fail to load!**


<h3>And that's it!<h3>
<h4>
I hope this guide makes sense. If you still have a confusion, check out example folder.
And I, wish you goodluck monetizing your pygame, android projects!
<h4>

**<h1> DONT FORGET TO USE TEST IDS WHEN TESTING. GOOGLE WILL BAN YOUR ACCOUNT**<h1>


				












