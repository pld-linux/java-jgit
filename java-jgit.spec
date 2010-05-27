
%include	/usr/lib/rpm/macros.java

%define		srcname		jgit
Summary:	Pure Java library implementing the Git
Summary(pl.UTF-8):	Biblioteka jezyka java implementująca Git
Name:		java-jgit
Version:	0.7.1
Release:	0.1
License:	EDL
Group:		Libraries/Java
Source0:	http://download.eclipse.org/jgit/maven/org/eclipse/jgit/org.eclipse.jgit/%{version}/org.eclipse.jgit-%{version}.jar
# Source0-md5:	0d5feb2d784b467798655c2ca9fc86d9
URL:		http://eclipse.org/jgit/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JGit is an EDL (new-style BSD) licensed, lightweight, pure Java
library implementing the Git version control system:

- repository access routines
- network protocols
- core version control algorithms

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar
