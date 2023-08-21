#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    int size, i;
    Py_ssize_t allocated;

    if (p && PyObject_HasAttrString(p, "append")) {
        size = (int)PyObject_Length(p);
        allocated = ((PyListObject *)p)->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %zd\n", allocated);

        for (i = 0; i < size; i++) {
            PyObject *element = PyList_GetItem(p, i);
            printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *data;

    if (p && PyObject_HasAttrString(p, "decode")) {
        size = PyObject_Length(p);
        data = (unsigned char *)PyBytes_AsString(p);

        printf("[.] bytes object info\n");
        printf("  size: %zd\n", size);
        PyObject *decoded = PyObject_Repr(p);
        PyObject *decoded_bytes = PyUnicode_AsEncodedString(decoded, "utf-8", "replace");
        printf("  trying string: %s\n", PyBytes_AsString(decoded_bytes));
        Py_XDECREF(decoded_bytes);
        Py_XDECREF(decoded);
        printf("  first 10 bytes: ");
        for (i = 0; i < 10 && i < size; i++) {
            printf("%02x", data[i]);
            if (i < size - 1)
                printf(" ");
        }
        printf("\n");
    } else {
        printf("[ERROR] Invalid Bytes Object\n");
    }
}

int main(void) {
    PyObject *s, *b, *l;

    Py_Initialize();

    s = PyBytes_FromStringAndSize("Hello", 5);
    b = PyBytes_FromStringAndSize("\xff\xf8\x00\x00\x00\x00\x00\x00", 8);
    l = PyList_New(0);
    PyList_Append(l, s);
    PyList_Append(l, b);

    print_python_bytes(s);
    print_python_bytes(b);
    print_python_list(l);

    Py_XDECREF(s);
    Py_XDECREF(b);
    Py_XDECREF(l);

    Py_Finalize();

    return (0);
}

