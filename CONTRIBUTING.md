# Contributing

Bug reports, feature requests, and pull requests are always welcome and encouraged! Thanks for choosing to help out on the project.

See the [`issue templates`](./.github/ISSUE_TEMPLATE/) for various templates

Don't be afraid to contribute! Check out [this](https://www.drmaciver.com/2015/04/its-ok-for-your-open-source-library-to-be-a-bit-shitty/) blog post for some moral support. Remember, your code doesn't have to be perfect the first time. That's why it's open source: so other people can help you out. (Please read the [Code of Conduct](./CODE_OF_CONDUCT.md))

# Readability

Try as much as possible to keep the root directory of this project clean. Group files into folders based on their function.

Writing code is the easy part. Showing other people how it works and remembering how it works yourself when you go back to look at it months later is the hard part. The solution is comments. Please try your best to thoroughly comment your code. Comments make contributing and maintaining code easier for everyone in the future.

# Encoding and Formatting

Contributions must meet the following requirements:

- Use Unicode UTF-8
- Use LF newline characters. (See [wikipedia](https://en.wikipedia.org/wiki/Newline) for an explanation)
- Use Tabs for indentation. Modern text editors have packages for batch-converting spaces to tabs. Use them.

# Bug Reports

Bug reports are not READMEs. Do not abstract any content. Provide as much information as possible to help reproduce the error.

_**Before opening an issue, make sure to set up all your dependencies properly and be running the latest version of the software, then run your own tests and try to do your own debugging first.**_

The best debugging is following the scientific method. First outline your hypothesis, then your materials, procedure, results, and your conclusion. By completing a scientific experiment, other developers will be provided with more information to help solve the issue.

# Feature Requests

Don't ever be afraid to suggest a feature. You can never know if someone else is also looking for that. But be conscious of other feature requests, try not to request the same thing twice. Note that here, following the feature request template is encouraged, but not strictly required.

## Caching

Caching can be difficult to deal with. Please reach out to me, [Sean Christians](https://github.com/seanchristians) if you have any suggestions. At present, the cache has these known issues:

- The cache is never cleared of old items
- Cached items are kept in use for 6 months. This seems reasonable, but no research has been conducted. Such as: how often does thesaurus.com add new words/change their results formula?
- Maybe the cache should be backed up?
- Maybe a cache of pre-computed results should be included with the project?

## Languages

Thanks for helping out with translation! There are many features to work on, such as:

- Expanding `extract.legal` to include support for more languages
- Adding support for more than one thesaurus website
- Translating error messages for different locales

## API

I'd love to get in contact with anyone who'd like to work on moving this code onto an official website and writing an API to dynamically interact with the project. Don't be afraid to contact [me](https://github.com/seanchristians)!