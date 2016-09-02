## 2016-09-02 v0.0.3
 - Instead of sorting the "derive" and "userDefinedFunctions" config dicts at use, now sort them in the top-level function dwmAll. This means, if you're running 10 fields for 1000 contacts, instead of calling ```sorted()``` 18,000 times, you call it 18 times at the very beginning to created OrderedDict.
 - Moved all references to setting/returning record-level history into the "config" object

## 2016-08-24 v0.0.2
 - Initial release
