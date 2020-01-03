class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
  setNext(next) {
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.length = 0;
  }

  // O(1)
  addToHead(data) {
    // Create new node
    const node = new Node(data);
    // Have new node point to old head
    node.setNext(this.head);
    // Set LinkedList head to new node
    this.head = node;
    // Increase length
    this.length++;
  }

  // DISPLAY O(n)
  displayAll() {
    let current = this.head;
    while (current) {
      current = current.next;
    }
    // TODO:
  }

  // SEARCH O(n)
  search(data) {
    let current = this.head;
    while (current) {
      if (current.data === data) {
        return current;
      }
      current = current.next;
    }
    return -1
  }
}

const list = new LinkedList();

list.addToHead(1);
list.addToHead(2);

console.log(list.search(3));
