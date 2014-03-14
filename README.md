Android whitelists
==================

This is a patchset for Android 4.3 (build JSS15J) that adds a protection scheme
against the threats caused by dynamically loaded external code. See [the
corresponding paper at
NDSS](http://seclab.cs.ucsb.edu/media/uploads/papers/2014_ndss_android-remote-code-execution.pdf)
or [this blog
post](http://blog.iseclab.org/2014/03/06/execute-this-looking-at-code-loading-techniques-in-android/)
for more information.

To try it out, get the
[sources](https://source.android.com/source/building.html) for Android build
JSS15J and make sure that you can compile the system. Then apply the patches
to the respective subdirectories (e.g., apply frameworks\_base.patch to
frameworks/base in your Android sources). After building the system, you should
only be able to run system apps. All others will be blocked by the protection
system.

In order to allow additional code, you have to whitelist it (this is where the
verification providers that we suggest in the paper come into play). Use the
script create.py to translate a file containing SHA1 hashes into our binary
representation. Then copy the result over to /data/whitelist/ on your device. It
will be detected and loaded immediately.
