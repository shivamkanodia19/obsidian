# Spring 2026 Final Cheat Sheet

This sheet is built from:
- `Final Exam Sample.pdf`
- `Final Exam Review - Spring 2026 (2).pdf`

Use it like a decision tree, not like a textbook. On the exam, most points come from:
- tracing what code prints
- deciding whether code leaks memory
- deciding which function version is called
- writing linked-list and vector-processing functions cleanly

---

## 1. Universal Code-Tracing Workflow

For any tracing problem, do these in order:

1. Mark every object with its type.
2. Mark every pointer/reference with what it points/refers to.
3. Circle whether each parameter is:
   - by value: copy
   - by reference: alias
   - pointer by value: copied address
4. For each function call, ask:
   - Is this overload resolution?
   - Is this template substitution?
   - Is this virtual dispatch?
5. For each `new`, ask:
   - Who owns this memory?
   - Is there a matching `delete` or `delete[]`?
6. For each recursive call, stop only when you hit the base case.

Fast rule:
- If you ever feel lost, draw boxes for stack objects and circles for heap objects.

---

## 2. Static vs. Dynamic Binding

### Core rule

If the base class function is `virtual`, the call depends on the actual object type.

If the base class function is not `virtual`, the call depends on the pointer/reference/object type used in the call.

### Decision tree

When you see `ptr->f()` or `ref.f()`:

1. Is `f` virtual in the base class?
   - Yes: use the actual object type.
   - No: use the static type of `ptr` or `ref`.
2. Was there object slicing earlier?
   - If yes, the object may already be just a base object.
3. Is scope resolution used, like `obj.Base::f()`?
   - If yes, virtual dispatch is bypassed.

### Default arguments and virtual functions

Default arguments are selected from the static type, but the function body is selected using virtual dispatch.

```cpp
class A {
public:
    virtual void f(int x = 10) { cout << "A" << x; }
};
class B : public A {
public:
    void f(int x = 20) override { cout << "B" << x; }
};

A* p = new B();
p->f();   // prints B10
```

Why:
- the default argument comes from `A*`, so `10`
- the virtual call reaches `B::f`, so `B`

### Must-know patterns

#### Pattern A: virtual + pointer/reference

```cpp
class A {
public:
    virtual void f() { cout << "A"; }
};
class B : public A {
public:
    void f() override { cout << "B"; }
};

B b;
A* p = &b;
A& r = b;
```

- `p->f()` prints `B`
- `r.f()` prints `B`

#### Pattern B: slicing

```cpp
B b;
A x = b;
x.f();
```

- `x` is now a separate `A` object
- the `B` part is cut off
- even if `f` is virtual, `x.f()` uses `A::f()`

#### Pattern C: no virtual

```cpp
class A {
public:
    void f() { cout << "A"; }
};
class B : public A {
public:
    void f() { cout << "B"; }
};

B b;
A* p = &b;
A& r = b;
```

- `b.f()` prints `B`
- `p->f()` prints `A`
- `r.f()` prints `A`

Reason: static binding uses the declared type `A*` or `A&`.

#### Pattern D: scope resolution

```cpp
A.foo::fun();
p->Parent::speak();
```

- this forces that exact class version
- virtual lookup is ignored

---

## 3. Inheritance and Access

### Member access table

Inside a derived member function:

| Base member | Accessible? |
| --- | --- |
| `public` | Yes |
| `protected` | Yes |
| `private` | No |

From `main` through an object:

| Member | Accessible? |
| --- | --- |
| `public` | Yes |
| `protected` | No |
| `private` | No |

### Inheritance mode changes visibility

If class `B` inherits from `A`:

| Inheritance | `A` public becomes | `A` protected becomes |
| --- | --- | --- |
| `public` | public | protected |
| `protected` | protected | protected |
| `private` | private | private |

Base `private` members are never directly accessible in the child.

### Exam traps

- A child can access a base `protected` member.
- `main` cannot access `protected`.
- A child cannot access a base `private` member directly.
- With `protected` inheritance, something that started `public` in the base may no longer be public from `main`.

---

## 4. Constructors, Abstract Classes, and Overriding

### Constructor and destructor order

When creating a derived object:

1. base constructor runs first
2. derived constructor runs second

If the derived constructor does not explicitly call a base constructor, the base default constructor is used.

When destroying a derived object:

1. derived destructor runs first
2. base destructor runs second

Construction is `Base -> Derived`. Destruction is `Derived -> Base`.

### Virtual calls in constructors and destructors

Virtual dispatch does not work the usual way inside constructors or destructors. During a base constructor or destructor, the object behaves like that base part, not like the most-derived object.

```cpp
class A {
public:
    A() { f(); }
    virtual void f() { cout << "A"; }
};
class B : public A {
public:
    void f() override { cout << "B"; }
};

B b;   // prints A
```

### Abstract classes

A class is abstract if it has at least one pure virtual function:

```cpp
virtual void print() const = 0;
```

Consequences:
- You cannot create objects of the abstract class.
- You can have pointers/references to it.
- A derived class must implement every inherited pure virtual function, or it also stays abstract.

### What derived must vs. can override

- If a base function is pure virtual: derived must implement it to become concrete.
- If a base function is regular virtual: derived can override it, but does not have to.

### Containers with polymorphism

Do not store abstract base objects directly:

```cpp
vector<Base> v;      // bad for abstract classes, slices derived objects
vector<Base*> v;     // good on this exam
```

Use base-class pointers when storing mixed derived types.

---

## 5. Object Slicing

### Trigger

Any time a derived object is assigned into a base object variable:

```cpp
Base b = derivedObj;
Base x = *ptrToDerived;
```

### What happens

- Only the base portion is copied.
- Derived data is discarded.
- The new object is a real `Base` object.

### Exam consequence

If later you call a virtual function on the sliced object, it still uses the base version, because the object itself is base now.

### Quick comparison

```cpp
Base x = derived;   // slicing
Base& y = derived;  // alias, no slicing
Base* z = &derived; // alias, no slicing
```

- `x.f()` uses `Base`
- `y.f()` may use `Derived` if virtual
- `z->f()` may use `Derived` if virtual

### Value parameter vs reference parameter

```cpp
void f(Base b);   // slicing on call
void g(Base& b);  // polymorphism preserved
```

Passing by value creates a base copy. Passing by reference keeps the original object.

---

## 6. Heap, Stack, and Pointer Logic

### What lives where?

| Expression | Usually on |
| --- | --- |
| local variable `int a;` | Stack |
| local pointer `int* p;` | Stack |
| local object `Box b;` | Stack |
| `new int{5}` | Heap |
| `new Box()` | Heap |
| member inside a stack object | same place as the object |

### Key trap

The pointer variable and the thing it points to are not in the same place.

Example:

```cpp
int* p = new int{7};
```

- `p` is on the stack
- `*p` is on the heap

### For arrow chains

Do not guess based on `->`.

Ask:
- where is this pointer variable stored?
- where is the pointee stored?

Example:

```cpp
class X {
    int* p;
};
X obj;
```

- `obj` is on stack
- `obj.p` is stored inside `obj`, so stack
- `*(obj.p)` is wherever `p` points, often heap

---

## 7. Parameter Passing: Value vs. Reference vs. Pointer

### By value

```cpp
void f(int x)
```

- copy
- changing `x` does not change caller

### By reference

```cpp
void f(int& x)
```

- alias
- changing `x` changes caller

### Pointer by value

```cpp
void f(int* p)
```

- the address is copied
- `*p = ...` changes caller's pointee
- `p = new int{...}` changes only the local copy of the pointer

This is one of the biggest exam traps.

### Reference to pointer

```cpp
void f(int*& p)
```

- now reassigning `p` changes the caller's pointer

If you do not see `&` on the pointer parameter itself, reassigning the pointer does not escape the function.

---

## 8. Memory Leaks, Dangling Pointers, and Rule of 3

### Memory leak checklist

For each `new` ask:
- Is there a matching `delete`?
- Is there a matching `delete[]` for `new[]`?
- Did we lose the address before deleting it?
- Was a heap object itself leaked because the pointer to the object was never deleted?

### Classic leak patterns

#### Pattern A: `new` without `delete`

```cpp
int* p = new int{5};
```

If no later `delete p;`, leak.

#### Pattern B: pointer reassigned locally

```cpp
void adjust(int* x) {
    x = new int[4];
}
```

- caller's pointer is unchanged
- new array inside `adjust` is leaked unless deleted before return

#### Pattern C: heap object itself not deleted

```cpp
Box* b = new Box();
```

If `delete b;` never happens, the `Box` object leaks.

### Dangling pointer is not always a leak

```cpp
int* c = new int{3};
delete c;
```

No leak, but `c` is dangling after delete.

### Rule of 3

If a class owns dynamic memory, it usually needs:
- destructor
- copy constructor
- copy assignment operator

If one is missing, default shallow copying can cause:
- aliasing
- double delete
- stale/dangling pointers
- unexpected shared changes

### Copy constructor vs. copy assignment

```cpp
Box a = b;   // copy constructor
a = b;       // copy assignment
```

Do not mix these up on the exam.

### Exam trap from the sample

If a class defines a deep-copy constructor but not a deep-copy assignment operator, then:

```cpp
*b = a;
```

may still do a shallow copy, because assignment is not the copy constructor.

---

## 9. Deleting Through a Base Pointer

### Safe rule

If a base class will ever be deleted through a base pointer, the base destructor should be `virtual`.

```cpp
class Base {
public:
    virtual ~Base() {}
};
```

### Trap

```cpp
Base* p = new Derived();
delete p;
```

If `Base::~Base()` is not virtual:
- only the base destructor runs
- derived cleanup is skipped
- derived-owned heap memory leaks

### Exam shortcut

When you see:
- inheritance
- dynamic allocation
- `Base* p = new Derived(...)`
- `delete p;`

immediately check whether the base destructor is virtual.

---

## 10. Overloading, Overriding, and Templates

### Overloading

Same function name, different parameter types.

```cpp
double func(double);
double func(int);
```

The compiler chooses using argument types at compile time.

### Trace nested overloads inside-out

```cpp
cout << func(func(15));
```

1. Inner call uses `int`, so choose `func(int)`.
2. Its return type becomes the argument type for the outer call.
3. Then choose the outer overload.

### Overriding

Same signature in derived class, with virtual dispatch from base.

### Exact signature required

To override, the signature must match exactly.

```cpp
class A {
public:
    virtual void f(int);
};
class B : public A {
public:
    void f(double);  // not an override
};
```

If the parameter types differ, the derived function does not override the base version.

### Function hiding

A derived function with the same name but different parameters hides the base overloads of that name.

```cpp
class B : public A {
public:
    void f(double);
};

B b;
b.f(5);   // may not see A::f
```

Use `A::f(...)` or `using A::f;` if the base overloads need to stay visible.

### Meaning of `override`

- `override` is optional.
- It does not change runtime behavior.
- It asks the compiler to verify that you really overrode a base virtual function.
- It helps catch signature mismatches early.

### Templates

Substitute the actual type first.

```cpp
template <typename T>
double func(T x) {
    return x / 2;
}
```

- `func(3)` means `T = int`, so `3 / 2` is integer division, result `1`, then converted to `1.0`
- `func(3.0)` means `T = double`, so result `1.5`

### Parametric polymorphism checklist

1. Find `T`.
2. Replace `T` everywhere.
3. Re-evaluate arithmetic using that real type.

---

## 11. Operator Overloading

Trace overloaded operators like normal functions.

### Example

```cpp
Num operator+(const Num& other) const {
    return Num(x + other.x, y);
}
```

Do not assume both fields are combined just because it is `+`.

Ask:
- what fields are actually used?
- what new object is returned?
- what does `operator<<` print?

If `operator<<` does:

```cpp
os << n.x << n.y;
```

then it prints the two values back-to-back with no space.

---

## 12. `stringstream` and Extraction

### Rule

`>>` extraction stops when it hits something invalid for the target type.

### For integers

```cpp
stringstream ss("11 * 12 + 13");
int x;
while (ss >> x) { ... }
```

- reads `11`
- next token starts with `*`
- extraction fails
- loop stops immediately

So only `11` contributes.

### Exam shortcut

If parsing into `int`, the first non-numeric character can stop the whole loop unless it is skipped as whitespace before a valid integer.

---

## 13. Recursion

### Tracing procedure

1. Find the base case.
2. Find the recursive step.
3. Expand calls until you hit the base case.
4. Return back upward one layer at a time.

### Common exam patterns

#### Pattern A: doubling until threshold

```cpp
int mystery(int x) {
    if (x > 8) return x;
    return mystery(x * 2);
}
```

Trace:
- `1 -> 2 -> 4 -> 8 -> 16`
- base case triggers at `16`

#### Pattern B: Collatz-style

```cpp
if (n % 2 == 0) return 1 + foo(n/2);
if (n == 1) return 1;
return 1 + foo(3*n + 1);
```

Do not skip steps. Write every value of `n`.

### Base case warning

A base case is not "the first `if`". It is the condition that stops recursion without another recursive call.

---

## 14. Exceptions and Overflow

### Exception rule

Once `throw` executes:
- the current function stops immediately
- later statements in that function do not run

### Overflow trap

A check can overflow too.

Example:

```cpp
if (x > INT_MAX - y)
```

This is not automatically safe if `y` is negative, because `INT_MAX - y` may overflow.

### Safer signed-addition pattern

```cpp
if ((y > 0 && x > INT_MAX - y) ||
    (y < 0 && x < INT_MIN - y)) {
    throw invalid_argument("Overflow!");
}
```

### Exam shortcut

If the code tries to protect against overflow, inspect the guard itself for undefined behavior.

---

## 15. Linked List Writing Patterns

These are the main code-writing styles from the review and sample.

### A. Traversal skeleton

```cpp
Node* curr = head;
while (curr != nullptr) {
    // use curr->value
    curr = curr->next;
}
```

### B. Average of list

Plan:
1. If empty, throw.
2. Traverse once.
3. Track `sum` and `count`.
4. Return average.

Skeleton:

```cpp
if (head == nullptr) {
    throw ...;
}
double sum = 0;
int count = 0;
Node* curr = head;
while (curr != nullptr) {
    sum += curr->value;
    count++;
    curr = curr->next;
}
return sum / count;
```

### C. Remove all maximum values

Best exam plan:
1. If empty, return.
2. First pass: find max value.
3. Remove matching nodes from the front.
4. Traverse the rest with `prev` and `curr`.

Skeleton:

```cpp
if (head == nullptr) return;

int mx = head->value;
Node* curr = head->next;
while (curr != nullptr) {
    if (curr->value > mx) mx = curr->value;
    curr = curr->next;
}

while (head != nullptr && head->value == mx) {
    Node* temp = head;
    head = head->next;
    delete temp;
}

Node* prev = head;
curr = (head == nullptr ? nullptr : head->next);
while (curr != nullptr) {
    if (curr->value == mx) {
        prev->next = curr->next;
        delete curr;
        curr = prev->next;
    } else {
        prev = curr;
        curr = curr->next;
    }
}
```

### D. Reverse list

Three-pointer pattern:

```cpp
Node* prev = nullptr;
Node* curr = head;
while (curr != nullptr) {
    Node* next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
}
head = prev;
```

### E. Middle of list

Use slow/fast pointers:

```cpp
Node* slow = head;
Node* fast = head;
while (fast != nullptr && fast->next != nullptr) {
    slow = slow->next;
    fast = fast->next->next;
}
return slow;
```

If empty, return `nullptr`.

### F. Detect cycle

Floyd's tortoise and hare:

```cpp
Node* slow = head;
Node* fast = head;
while (fast != nullptr && fast->next != nullptr) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) return true;
}
return false;
```

### G. Swap evens between two lists

The cleanest exam-safe idea:
- traverse each list to the next even-valued node
- when both exist, swap their `data` values
- continue
- stop when either list runs out of even nodes

This avoids pointer surgery and avoids allocating memory.

Skeleton:

```cpp
Node* a = head;
Node* b = other.head;

while (true) {
    while (a != nullptr && a->value % 2 != 0) a = a->next;
    while (b != nullptr && b->value % 2 != 0) b = b->next;

    if (a == nullptr || b == nullptr) return;

    int temp = a->value;
    a->value = b->value;
    b->value = temp;

    a = a->next;
    b = b->next;
}
```

Why this is great on an exam:
- correct final list values
- no allocation
- no leak risk
- no head-update complexity

---

## 16. Vector / Struct Processing Pattern

From the sample `process_structs` problem.

### Problem type

Input:
- vector of structs

Output:
- 2-D vector built from each struct
- invalid structs skipped
- rows trimmed to rectangular shape

### Plan

1. Create output vector.
2. Track shortest valid row length seen so far.
3. For each struct:
   - if `min > max`, skip it
   - otherwise create row from `min` to `max`
   - push row into output
   - update shortest length
4. After processing, trim every row to the shortest length.

### Skeleton

```cpp
vector<vector<int>> out;
bool have_row = false;
int shortest = 0;

for (int i = 0; i < input.size(); i++) {
    if (input[i].min > input[i].max) continue;

    vector<int> row;
    for (int x = input[i].min; x <= input[i].max; x++) {
        row.push_back(x);
    }

    if (!have_row || row.size() < shortest) {
        shortest = row.size();
        have_row = true;
    }

    out.push_back(row);
}

for (int i = 0; i < out.size(); i++) {
    while (out[i].size() > shortest) {
        out[i].pop_back();
    }
}

return out;
```

### Edge case

If every struct is invalid, return an empty 2-D vector.

---

## 17. Common Print Outputs from This Review Style

### Virtual dispatch + slicing combo

```cpp
B* ptr = new B();
A x = *ptr;
A& y = *ptr;
A* z = ptr;
x.f();
y.f();
z->f();
```

If `f` is virtual:
- `x.f()` uses `A`
- `y.f()` uses `B`
- `z->f()` uses `B`

### Non-virtual version

Same code, but `f` not virtual:
- `x.f()` uses `A`
- `y.f()` uses `A`
- `z->f()` uses `A`

### Pointer parameter trap

```cpp
void f(int* p) {
    p = new int{9};
}
```

Caller's pointer does not change.

### Reference parameter trap

```cpp
void f(int& x) {
    x = 9;
}
```

Caller's variable does change.

### Vector pass-by-value trap

```cpp
void f(vector<int>& a, vector<int> b)
```

- changes to `a` affect caller
- changes to `b` do not

---

## 18. True/False Style Reminders

### Pointer equality vs. object equality

```cpp
a1 == a2
```

For pointers, this compares addresses, not object contents.

Two separate `new Animal("Tod", 10)` calls usually produce different addresses, so `a1 == a2` is false.

### Aliases

```cpp
Animal* a3 = a1;
```

Now `a3 == a1` is true because both store the same address.

### Can you default-construct?

If the class only defines a constructor with parameters and no default constructor:

```cpp
Animal a5;
```

does not compile.

But if the class has a zero-argument constructor, it does.

### Can `<<` print an object directly?

Only if an `operator<<` overload exists for that type.

This:

```cpp
cout << a4;
```

usually fails unless overload provided.

This:

```cpp
cout << a4.getName();
```

works if `getName()` returns a printable type like `string`.

### Container slicing vs polymorphism

```cpp
vector<Base> v;    // slices derived objects
vector<Base*> v;   // preserves polymorphism
```

---

## 19. What to Write for Partial Credit on Code Questions

The review explicitly says partial credit matters. If stuck:

1. Write the function signature correctly.
2. Write the empty-list / base-case handling first.
3. Write variable declarations with meaningful names.
4. Add 1-2 short comments showing your plan.
5. Handle head updates carefully in linked lists.
6. Avoid fancy tricks if a straightforward loop works.

Good comment style:

```cpp
// first pass: find maximum value
// second pass: remove every node storing that value
```

Bad comment style:

```cpp
// this variable stores a variable
```

---

## 20. Fast Final Checklist

Before locking an answer, ask:

- Is the called function `virtual`?
- Is this object sliced?
- Is scope resolution forcing a specific base version?
- Is a parameter passed by value, reference, or pointer?
- Did a pointer reassignment actually affect the caller?
- Does every `new` have a matching `delete` or `delete[]`?
- Is a base pointer deleting a derived object without a virtual destructor?
- Am I comparing addresses or values?
- Did template substitution change integer vs. floating-point arithmetic?
- Does `stringstream >> int` stop at the first bad token?
- Did the recursive call really reach a base case?
- For linked lists: did I handle empty list, head removal, and `nullptr` safely?

---

## 21. Last-Minute Memory Anchors

If you only remember a few things, remember these:

- `virtual` means actual object type matters.
- no `virtual` means declared pointer/reference type matters.
- `Base x = derived;` slices.
- `int* p` passed by value cannot be permanently reassigned for the caller.
- `*p = ...` changes the pointee, `p = ...` changes only the local pointer copy.
- `protected` is visible in children, not in `main`.
- base `private` is never directly visible in children.
- local variables live on stack, `new` allocates on heap.
- `new[]` pairs with `delete[]`.
- deleting through `Base*` needs a virtual base destructor.
- templates keep the arithmetic behavior of the substituted type.
- `stringstream >> int` stops when extraction fails.
- for list problems, simple pointer loops beat clever code.
