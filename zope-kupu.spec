%define product		kupu
%define realVersion     1.3.9
%define release         1

%define version %(echo %{realVersion} | sed -e 's/-/./g')

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	Kupu is a cross-browser WYWSIWYG editor
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	BSDish
Group:		System/Servers
Source:		http://plone.org/products/kupu/releases/%{version}/kupu.tar.bz2
Patch0:		kupu-python-version.patch
URL:		http://plone.org/products/kupu/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}

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
%patch0 -p0

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
%defattr(-, root, root, 0755)
%{software_home}/Products/*




