(window.webpackJsonp=window.webpackJsonp||[]).push([[12],{508:function(n,e,t){"use strict";t.r(e);var r={data:function(){return{markdown:"\n\n\n@startuml\n\nnode UFS {\n  interface AutoScaling\n  interface Compute\n  interface ELB\n}\nnode CLC {\n  database DB\n}\nAutoScaling ..> Compute\nAutoScaling ..> ELB\nAutoScaling --\x3e DB\n@enduml\n\n# h1 Heading\n## h2 Heading\n### h3 Heading\n#### h4 Heading\n##### h5 Heading\n###### h6 Heading\n\n## Emphasis\n\n**This is bold text**\n\n__This is bold text__\n\n*This is italic text*\n\n_This is italic text_\n\n~~Strikethrough~~\n\n## Blockquotes\n\n\n> Blockquotes can also be nested...\n>> ...by using additional greater-than signs right next to each other...\n> > > ...or with spaces between arrows.\n\n## Lists\n\nUnordered\n\n+ Create a list by starting a line with '+', '-', or '*'\n+ Sub-lists are made by indenting 2 spaces:\n  - Marker character change forces new list start:\n    * Ac tristique libero volutpat at\n    + Facilisis in pretium nisl aliquet\n    - Nulla volutpat aliquam velit\n+ Very easy!\n\nOrdered\n\n1. Lorem ipsum dolor sit amet\n2. Consectetur adipiscing elit\n3. Integer molestie lorem at massa\n\n\n1. You can use sequential numbers...\n1. ...or keep all the numbers as '1.'\n\nStart numbering with offset:\n\n57. foo\n1. bar\n      "}}},o=t(92),component=Object(o.a)(r,(function(){var n=this,e=n.$createElement;return(n._self._c||e)("div",{domProps:{innerHTML:n._s(n.$md.render(n.markdown))}})}),[],!1,null,null,null);e.default=component.exports}}]);