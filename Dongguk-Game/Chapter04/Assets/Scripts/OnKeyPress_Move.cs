using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnKeyPress_Move : MonoBehaviour
{

    public float speed = 2; // �ӵ�: Inspector�� ����

    float vx = 0;
    float vy = 0;
    bool leftFlag = false;
    Rigidbody2D rbody;

    // Start is called before the first frame update
    void Start()    // ó���� �����Ѵ�.
    {
        // �߷��� 0���� �ؼ� �浹 �ÿ� ȸ����Ű�� �ʴ´�
        rbody = GetComponent<Rigidbody2D>();
        rbody.gravityScale = 0;
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    // Update is called once per frame
    void Update()   // ��� �����Ѵ�.0
    {
        vx = 0;
        vy = 0 ;

        if (Input.GetKey("right"))  // ���� ������ Ű�� ������
        {
            vx = speed; // ���������� ���ư��� �̵����� �ִ´�.
            leftFlag = false;
        }
        if (Input.GetKey("left"))   // ���� ���� Ű�� ������
        {
            vx = -speed; // �������� ���ư��� �̵����� �ִ´�
            leftFlag = true;
        }
        if (Input.GetKey("up"))     // ���� �� Ű�� ������
        {
            vy = speed; // ���� ���ư��� �̵����� �ִ´�
        }
        if (Input.GetKey("down"))   // ���� �Ʒ� Ű�� ������
        {
            vy = -speed; // �Ʒ��� ���ư��� �̵����� �ִ´�
        }
    }

    private void FixedUpdate()  // ��� �����Ѵ�(���� �ð�����)
    {
        // �̵��Ѵ�
        rbody.velocity = new Vector2 (vx, vy);
        // ���� ������ ������ �ٲ۴�
        this.GetComponent<SpriteRenderer>().flipX = leftFlag;
    }
}
