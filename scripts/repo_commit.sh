# https://github.com/karma-runner/karma/commits/master 
#================================================================================
# COMMIT GENERALIZED FORMAT
#================================================================================
    # <type>(<scope>): <subject>
    # <body>
    # <footer>
    # Cc: Z
    # Reviewed-by: Z
    # Signed-off-by: Bob <bob@example.com>
    # Acked-by: Alice <alice@example.com>
#================================================================================
# COMMIT TYPE
#================================================================================
    # build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
    # chore : "(updating grunt tasks etc; no production code change)",
    # ci: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
    # docs : "(changes to the documentation)",
    # feat : "(new feature for the user, not a new feature for build script)",
    # fix : "(bug fix for the user, not a fix to a build script)",
    # perf: A code change that improves performance
    # refactor : "(refactoring production code, eg. renaming a variable)",
    # revert: "(commit reverted.)",
    # style : "(formatting, missing semi colons, etc; no production code change)",
    # test : "(adding missing tests, refactoring tests; no production code change)",
#================================================================================
# COMMIT SCOPE 
#================================================================================
    # $browser
    # $compile
    # $location
    # $rootScope
    # animations
    # common
    # compiler
    # compiler-cli
    # config
    # core
    # docs
    # docs-parser
    # elements
    # forms
    # http
    # init
    # language-service
    # ngClick
    # ngHref
    # ngView
    # platform-browser
    # platform-browser-dynamic
    # platform-server
    # platform-webworker
    # platform-webworker-dynamic
    # proxy
    # router
    # runner
    # scenario-runner
    # service-worker
    # upgrade
    # watcher
    # web-server
    # etc.
#================================================================================
# COMMIT FOOTER 
#================================================================================
    # Closes #123, #245, #992
    # Fix #42
    # Refs #133
    # See-also: fe3187489d69c4 (subject of related commit)
#================================================================================
# COMMIT SNIPPET 
#================================================================================
    #================================================================================    
    # revert: let us never again speak of the noodle incident

    # Refs: 676104e, a215868
    #================================================================================    
    # refactor!: drop support for Node 6
    #================================================================================    
    # feat($browser): onUrlChange event (popstate/hashchange/polling)
    # Added new event to $browser:
    # - forward popstate event if available
    # - forward hashchange event if popstate not available
    # - do polling when neither popstate nor hashchange available
    # Closes #392
    # Breaks $browser.onHashChange, which was removed (use onUrlChange instead)
#================================================================================
# COMMIT EXAMPLE 
#================================================================================

    # Capitalized, short (50 chars or less) summary

    # More detailed explanatory text, if necessary.  Wrap it to about 72
    # characters or so.  In some contexts, the first line is treated as the
    # subject of an email and the rest of the text as the body.  The blank
    # line separating the summary from the body is critical (unless you omit
    # the body entirely); tools like rebase can get confused if you run the
    # two together.

    # Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
    # or "Fixes bug."  This convention matches up with commit messages generated
    # by commands like git merge and git revert.

    # Further paragraphs come after blank lines.

    # - Bullet points are okay, too

    # - Typically a hyphen or asterisk is used for the bullet, followed by a
    # single space, with blank lines in between, but conventions vary here

    # - Use a hanging indent
#================================================================================
# COMMIT EXAMPLE BREAKING CHANGE
#================================================================================
    # BREAKING CHANGE:

    # `port-runner` command line option has changed to `runner-port`, so that it is
    # consistent with the configuration file syntax.

    # To migrate your project, change all the commands, where you use `--port-runner`
    # to `--runner-port`.

#================================================================================
# COMMIT EXAMPLE BREAKING CHANGE
#================================================================================
    # BREAKING CHANGE: isolate scope bindings definition has changed and
    #         the inject option for the directive controller injection was removed.
        
    #     To migrate the code follow the example below:
        
    #     Before:
        
    #     scope: {
    #       myAttr: 'attribute',
    #       myBind: 'bind',
    #       myExpression: 'expression',
    #       myEval: 'evaluate',
    #       myAccessor: 'accessor'
    #     }
        
    #     After:
        
    #     scope: {
    #       myAttr: '@',
    #       myBind: '@',
    #       myExpression: '&',
    #       // myEval - usually not useful, but in cases where the expression is assignable, you can use '='
    #       myAccessor: '=' // in directive's template change myAccessor() to myAccessor
    #     }
        
    #     The removed `inject` wasn't generaly useful for directives so there should be no code using it.
