using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using NUnit.Framework;

using System.Windows.Forms;

using stud_group;

namespace NUnitTest1

{

[TestFixture]

public class TestFixture1

{

[Test]

public void TestForm()

{

Form1 form = new Form1();

Assert.IsNotNull(form);

}

[Test]

public void TestLoadFile()

{

Form1 form = new Form1();

//Выбранный файл существует

int year = 2011;

string spec = "Информатика";

int kurs = 1;

string group = "1 группа";

string fname = year.ToString() + spec + kurs.ToString() + group;

ListBox lb = new ListBox();

Assert.IsTrue(form.LoadFile(fname, lb));

}

[Test]

public void TestLoadFileNot()

{

Form1 form = new Form1();

//Выбранный файл отсутствует

int year = 2022;

string spec = "Информатика";

int kurs = -1;

string group = "1 группа";

string fname = year.ToString() + spec + kurs.ToString() + group;

ListBox lb = new ListBox();

Assert.IsFalse(form.LoadFile(fname, lb));

}

[Test]

public void TestSaveFile()

{

Form1 form = new Form1();

//Выбранный файл существует

int year = 2011;

string spec = "Информатика";

int kurs = 1;

string group = "1 группа";

string fname = year.ToString() + spec + kurs.ToString() + group;

ListBox lb = new ListBox();

Assert.IsTrue(form.SaveFile(fname, lb));

}

[Test]

public void TestSaveFileNot()

{

Form1 form = new Form1();

//Выбранный файл отсутствует

int year = 2022;

string spec = "Информатика";

int kurs = -1;

string group = "1 группа";

string fname = year.ToString() + spec + kurs.ToString() + group;

ListBox lb = new ListBox();

Assert.IsFalse(form.LoadFile(fname, lb));

}

}

}