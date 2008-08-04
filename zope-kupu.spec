%define product	kupu
%define name    zope-%{product}
%define version 1.4.6
%define bad_version %(echo %{version} | sed -e 's/\\./-/g')
%define release %mkrel 5

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Cross-browser WYWSIWYG editor
License:	BSDish
Group:		System/Servers
URL:		http://plone.org/products/kupu/
Source:		http://plone.org/products/kupu/releases/%{version}/kupu-%{bad_version}.tgz
Requires:	zope >= %{zope_minver}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Kupu is a cross-browser WYWSIWYG editor. It allows the comfortable
editing of the body of an HTML document. It's client-side (browser)
requirements are one of Mozilla, Internet Explorer or Netscape Navigator.

Server-side can be useful for processing data (CGI or something more fancy
like PHP, ASP or Python scripts in Zope).

Kupu is particularly suited for content migration as well as editing.
Content copied from an existing web page is pasted with all formatting
intact. This includes structure such as headings and lists, plus links,
image references, text styling, and other aspects. Copying text from a
word processor with an HTML clipboard - such as MSWord - works exactly
the same.

Kupu will clean up the content before it is sent to the server, and can
send data to the server asynchronously using PUT (which allows the data
to be saved without reloading the page) as well as in a form.

Kupu can be customized on many different levels, allowing a lot of changes
from CSS, but also providing a JavaScript extension API.


%prep
%setup -c -q
find . -type f -name *.py -o -name *.cgi | xargs \
    perl -pi -e 's|#!/usr/bin/python.*|#!/usr/bin/python2.4|'


%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
