from fractions import Fraction


using System;

using System.Collections.Generic;

using System.ComponentModel;

using System.Data;

using System.Drawing;

using System.Linq;

using System.Text;

using System.Windows.Forms;

using System.IO;

namespace stud_group

{

public partial class Form1 : Form

{

public Form1()

{

InitializeComponent();

}

public bool LoadFile(string fname, ListBox lb)

//загрузка файла в Listbox

{

if (lb == null)

lb = listBox1;

if (!File.Exists(fname))//если файл не задан

{

StreamWriter g = new StreamWriter(fname, false, Encoding.Default);

g.WriteLine("нет данных");

g.Close();

return false;

}

StreamReader f = new StreamReader(fname, Encoding.Default);

string s;

lb.Items.Clear();

while (!f.EndOfStream)

{

s = f.ReadLine(); //читаем название теста

lb.Items.Add(s);

}

lb.SelectedIndex = 0;

f.Close();

f.Dispose();

return true;

}

public bool SaveFile(string fname, ListBox lb)

//сохранение данных из Listbox в файле

{

if (lb == null)

lb = listBox1;

StreamWriter g = new StreamWriter(fname, false, Encoding.Default);

int i;

for (i = 0; i < lb.Items.Count; i++)

g.WriteLine(lb.Items[i].ToString());

g.Close();

return true;

}

private void Form1_Load(object sender, EventArgs e)

//загрузка данных из файлов

{

StreamReader f = new StreamReader("god", Encoding.Default);

string s;

listBox1.Items.Clear();

while (!f.EndOfStream)

{

s = f.ReadLine(); //читаем название текста

listBox1.Items.Add(s);

}

listBox1.SelectedIndex = 0;

f.Close();

f.Dispose();

}

//------------------------------------------------------

private void listBox1_Click(object sender, EventArgs e)

//вывод выбранного года в поле редактирования

{

if (listBox1.SelectedIndex < 0) return;

textBox1.Text = listBox1.Items[listBox1.SelectedIndex].ToString();

LoadFile("spec" + listBox1.Items[listBox1.SelectedIndex].ToString(), listBox2);

}

private void AddGod_Click(object sender, EventArgs e)

//добавить год в список

{

if (textBox1.Text == "") return;

listBox1.Items.Add(textBox1.Text);

SaveFile("god", listBox1);

}

private void DelGod_Click(object sender, EventArgs e)

//удалить год из списка

{

if (listBox1.SelectedIndex < 0) return;

listBox1.Items.RemoveAt(listBox1.SelectedIndex);

SaveFile("god", listBox1);

}

private void SaveGod_Click(object sender, EventArgs e)

//сохранить результат редактирования года в списке

{

if (listBox1.SelectedIndex < 0) return;

if (textBox1.Text != "")

{

listBox1.Items[listBox1.SelectedIndex] = textBox1.Text;

SaveFile("god", listBox1);

}

}

//------------------------------------------------------

private void listBox2_Click(object sender, EventArgs e)

//вывод выбранной специальности в поле редактирования

{

if (listBox2.SelectedIndex < 0) return;

textBox2.Text = listBox2.Items[listBox2.SelectedIndex].ToString();

LoadFile(listBox1.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString(), listBox3);

}

private void AddSpec_Click(object sender, EventArgs e)

//добавить специальность в список

{

if (textBox2.Text == "") return;

listBox2.Items.Add(textBox2.Text);

SaveFile("spec" + listBox1.Items[listBox1.SelectedIndex].ToString(), listBox2);

}

private void DelSpec_Click(object sender, EventArgs e)

//удалить специальность из списка

{

if (listBox2.SelectedIndex < 0) return;

listBox2.Items.RemoveAt(listBox2.SelectedIndex);

SaveFile("spec" + listBox1.Items[listBox1.SelectedIndex].ToString(), listBox2);

}

private void SaveSpec_Click(object sender, EventArgs e)

//сохранить результат редактирования специальности в списке

{

if (listBox2.SelectedIndex < 0) return;

if (textBox2.Text != "")

{

listBox2.Items[listBox2.SelectedIndex] = textBox2.Text;

SaveFile("spec" + listBox1.Items[listBox1.SelectedIndex].ToString(), listBox2);

}

}

//------------------------------------------------------

private void listBox3_SelectedIndexChanged(object sender, EventArgs e)

//вывод выбранного курса в поле редактирования

{

if (listBox3.SelectedIndex < 0) return;

textBox3.Text = listBox3.Items[listBox3.SelectedIndex].ToString();

LoadFile(listBox1.SelectedIndex.ToString() +

listBox2.SelectedIndex.ToString() +

listBox3.SelectedIndex.ToString(), listBox4);

}

private void DelKurs_Click(object sender, EventArgs e)

//удалить курс из списка

{

if (listBox3.SelectedIndex < 0) return;

listBox3.Items.RemoveAt(listBox3.SelectedIndex);

SaveFile(listBox1.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString(), listBox3);

}

private void AddKurs_Click(object sender, EventArgs e)

//добавить курс в список

{

if (textBox3.Text == "") return;

listBox3.Items.Add(textBox3.Text);

SaveFile(listBox1.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString(), listBox3);

}

private void SaveKurs_Click(object sender, EventArgs e)

//сохранить результат редактирования курса в списке

{

if (listBox3.SelectedIndex < 0) return;

if (textBox3.Text != "")

{

listBox3.Items[listBox3.SelectedIndex] = textBox3.Text;

SaveFile(listBox1.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString(), listBox3);

}

}

//------------------------------------------------------

private void AddGrup_Click(object sender, EventArgs e)

//добавить группу в список

{

if (textBox4.Text == "") return;

listBox4.Items.Add(textBox4.Text);

SaveFile(listBox1.SelectedIndex.ToString() +

listBox2.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString(), listBox4);

}

private void DelGrup_Click(object sender, EventArgs e)

//удалить группу из списка

{

if (listBox4.SelectedIndex < 0) return;

listBox4.Items.RemoveAt(listBox4.SelectedIndex);

SaveFile(listBox1.SelectedIndex.ToString() +

listBox2.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString(), listBox4);

}

private void SaveGrup_Click(object sender, EventArgs e)

//сохранить результат редактирования группы в списке

{

if (listBox4.SelectedIndex < 0) return;

if (textBox4.Text != "")

{

listBox4.Items[listBox4.SelectedIndex] = textBox4.Text;

SaveFile(listBox1.SelectedIndex.ToString() +

listBox2.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString(), listBox4);

}

}

private void listBox4_SelectedIndexChanged(object sender, EventArgs e)

//вывод выбранной группы в поле редактирования

{

if (listBox4.SelectedIndex < 0) return;

textBox4.Text = listBox4.Items[listBox4.SelectedIndex].ToString();

}

//------------------------------------------------------

private void ListGrup_Click(object sender, EventArgs e)

//вывести список группы

{

Form2 f2 = new Form2();

string fname;

fname = listBox1.SelectedIndex.ToString() + listBox2.SelectedIndex.ToString() +

listBox3.SelectedIndex.ToString() + listBox4.SelectedIndex.ToString();

if (!File.Exists(fname))//если файл не задан

{

MessageBox.Show("Файл со списком студентов не найден. Создан пустой.", "Информация");

StreamWriter g = new StreamWriter(fname);

g.Close();

}

StreamReader f = new StreamReader(fname, Encoding.Default);

string s;

f2.cfname = fname;

f2.listBox1.Items.Clear();

while (!f.EndOfStream)

{

s = f.ReadLine();

f2.listBox1.Items.Add(s);

}

if (f2.listBox1.Items.Count != 0)

f2.listBox1.SelectedIndex = 0;

f.Close();

f2.label2.Text = listBox1.Items[listBox1.SelectedIndex].ToString() + " год, " +

listBox2.Items[listBox2.SelectedIndex].ToString() + ", " +

listBox3.Items[listBox3.SelectedIndex].ToString() + " курс, " +

listBox4.Items[listBox4.SelectedIndex].ToString();

f2.ShowDialog();

}

}

}

namespace stud_group

{

partial class Form2

{

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.IContainer components = null;

/// <summary>

/// Clean up any resources being used.

/// </summary>

/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>

protected override void Dispose(bool disposing)

{

if (disposing && (components != null))

{

components.Dispose();

}

base.Dispose(disposing);

}

#region Windows Form Designer generated code

/// <summary>

/// Required method for Designer support - do not modify

/// the contents of this method with the code editor.

/// </summary>

private void InitializeComponent()

{

System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form2));

this.label1 = new System.Windows.Forms.Label();

this.label2 = new System.Windows.Forms.Label();

this.listBox1 = new System.Windows.Forms.ListBox();

this.SaveEdit = new System.Windows.Forms.Button();

this.DelStud = new System.Windows.Forms.Button();

this.textBox1 = new System.Windows.Forms.TextBox();

this.AddStud = new System.Windows.Forms.Button();

this.SaveFile = new System.Windows.Forms.Button();

this.SuspendLayout();

//

// label1

//

this.label1.Dock = System.Windows.Forms.DockStyle.Top;

this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));

this.label1.Location = new System.Drawing.Point(0, 0);

this.label1.Name = "label1";

this.label1.Size = new System.Drawing.Size(373, 24);

this.label1.TabIndex = 0;

this.label1.Text = "Архив учебных групп";

this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;

//

// label2

//

this.label2.Dock = System.Windows.Forms.DockStyle.Top;

this.label2.Location = new System.Drawing.Point(0, 24);

this.label2.Name = "label2";

this.label2.Size = new System.Drawing.Size(373, 23);

this.label2.TabIndex = 1;

this.label2.Text = "label2";

this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;

//

// listBox1

//

this.listBox1.FormattingEnabled = true;

this.listBox1.Location = new System.Drawing.Point(12, 60);

this.listBox1.Name = "listBox1";

this.listBox1.Size = new System.Drawing.Size(348, 277);

this.listBox1.TabIndex = 2;

this.listBox1.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged);

//

// SaveEdit

//

this.SaveEdit.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));

this.SaveEdit.Image = ((System.Drawing.Image)(resources.GetObject("SaveEdit.Image")));

this.SaveEdit.Location = new System.Drawing.Point(75, 366);

this.SaveEdit.Name = "SaveEdit";

this.SaveEdit.Size = new System.Drawing.Size(29, 29);

this.SaveEdit.TabIndex = 8;

this.SaveEdit.UseVisualStyleBackColor = true;

this.SaveEdit.Click += new System.EventHandler(this.SaveEdit_Click);

//

// DelStud

//

this.DelStud.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));

this.DelStud.Image = ((System.Drawing.Image)(resources.GetObject("DelStud.Image")));

this.DelStud.Location = new System.Drawing.Point(44, 366);

this.DelStud.Name = "DelStud";

this.DelStud.Size = new System.Drawing.Size(29, 29);

this.DelStud.TabIndex = 7;

this.DelStud.UseVisualStyleBackColor = true;

this.DelStud.Click += new System.EventHandler(this.DelStud_Click);

//

// textBox1

//

this.textBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));

this.textBox1.Location = new System.Drawing.Point(13, 340);

this.textBox1.Name = "textBox1";

this.textBox1.Size = new System.Drawing.Size(347, 20);

this.textBox1.TabIndex = 6;

//

// AddStud

//

this.AddStud.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));

this.AddStud.Image = ((System.Drawing.Image)(resources.GetObject("AddStud.Image")));

this.AddStud.Location = new System.Drawing.Point(13, 366);

this.AddStud.Name = "AddStud";

this.AddStud.Size = new System.Drawing.Size(29, 29);

this.AddStud.TabIndex = 5;

this.AddStud.UseVisualStyleBackColor = true;

this.AddStud.Click += new System.EventHandler(this.AddStud_Click);

//

// SaveFile

//

this.SaveFile.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));

this.SaveFile.Image = ((System.Drawing.Image)(resources.GetObject("SaveFile.Image")));

this.SaveFile.Location = new System.Drawing.Point(128, 366);

this.SaveFile.Name = "SaveFile";

this.SaveFile.Size = new System.Drawing.Size(29, 29);

this.SaveFile.TabIndex = 9;

this.SaveFile.UseVisualStyleBackColor = true;

this.SaveFile.Click += new System.EventHandler(this.SaveFile_Click);

//

// Form2

//

this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);

this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;

this.ClientSize = new System.Drawing.Size(373, 401);

this.Controls.Add(this.SaveFile);

this.Controls.Add(this.SaveEdit);

this.Controls.Add(this.DelStud);

this.Controls.Add(this.textBox1);

this.Controls.Add(this.AddStud);

this.Controls.Add(this.listBox1);

this.Controls.Add(this.label2);

this.Controls.Add(this.label1);

this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;

this.MaximizeBox = false;

this.Name = "Form2";

this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;

this.Text = "Список группы";

this.ResumeLayout(false);

this.PerformLayout();

}

#endregion

private System.Windows.Forms.Label label1;

public System.Windows.Forms.Label label2;

public System.Windows.Forms.ListBox listBox1;

private System.Windows.Forms.Button SaveEdit;

private System.Windows.Forms.Button DelStud;

private System.Windows.Forms.TextBox textBox1;

private System.Windows.Forms.Button AddStud;

private System.Windows.Forms.Button SaveFile;

}

}