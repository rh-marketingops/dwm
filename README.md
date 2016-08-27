# dwm (Data Washing Machine)
Red Hat's business logic for maintaining marketing data quality

# Introduction

Database quality is a problem for many companies. Often there is a mad dash to collect as much data as possible before a single thought is given to keeping that data high quality. Some examples of bad input data include:

 - Data collection tools (such as interest or freemium forms) that require manual input, rather than OAuth or picklists
 - Ill-trained data entry or office staff
 - Data purchased from outside sources that does not conform with company standards

Bad data introduced through these sources can lead to significant amounts of lost time invested in manual correction, or directly to lost opportunities and revenue due to not being able to query on clean data.

This package was originally developed for use by Marketing Operations groups to maintain quality of contact data, although the principles are sound enough to apply to many types of databases. It is built for use with MongoDB to allow easier creation of custom frontend UIs.

# Business logic

The following are what we have determined to be the general "best practices" for maintaining data quality.

## Validation

Validation is the removal of data that is straight-up junk and provides no business value whatsoever. This data is usually the result of spam-bots, errors in collection tools (such as posting bad html strings), or someone uploading the wrong spreadsheet. We've split validation into two pieces: generic and field-specific.

### Generic

Generic validation is the removal of data that has no place in a given database, no matter what field it is found in. The following are examples of generic bad data:

```
aaaaaaaaaaaaaaa ## one repeated character
fdsafdasfdfdsafdafdsa ## all typed with left hand on the home line
buy levitra cialis ## spam data
www.buymystuff.com ## marketing database-specific example; our processes do not try to clean any website/URL related fields, so if this appears in one of the fields we are cleaning, it's probably bad data
```

### Field-Specific

Field-Specific validation is the removal of data that is junk in one field, but good data in another. An example is a string of nine numbers: ```9493020093```. In a phone number field, this is probably good data. In the First Name field, it's junk. Conversely, ```hi, this is a string of letters``` may have a purpose in a text-based field, but it provides no reasonable data in a phone number field.

## Normalization

Normalization is the correction of data to conform with a certain expected set of values. For example, ```Proggrrammer/Developer``` is almost a valid "Job Role" value ```Programmer/Developer```, but is mis-spelled. Another example is ```Programmer```, which obviously would fall into the previous category, but is not an exact value match.

Note that normalization usually cannot be applied to fields that are expected to be free-text, such as "First Name" or "Company Name". If certain rules need to be applied to those fields, use of the __User-Defined Functions__ is recommended.

## Derivation

Derivation is the management of fields designed to help business users more easily make decisions, but are not explicitly collected. One example is a "Super Region" field. Although "Country" is a value that is likely collected, users of the database may only need to filter to a general region to do their jobs.

## User-Defined Functions

The above three processes are the most common processes that need to be applied to data, but not everything can be planned for. User-Defined functionality is designed to fill this gap. For instance, US Zipcodes can have some fairly basic and consistent transformations applied to make the data easier to work with (i.e., strip off trailing hypen/number combos, left pad with 0s in case of bad spreadsheet formatting), but those rules don't fall into any of the above categories.

Also included may be thrid-party data enrichment. For example, if you have an API contract with a company that provides IP address geolocation, or provides additional company info based on email domain, you can define a function to interact with that API and pull additional data into the fields of interest.

# Architecture

## Cleaning Methods

### Lookups

### Regex

### Derivation Rules

## Data Flow

# Setup Process

# Examples
